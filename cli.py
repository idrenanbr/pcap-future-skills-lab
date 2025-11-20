from typing import Dict, List, Optional

from models import Competencia, Perfil, Carreira
from data import criar_competencias_padrao, criar_carreiras_padrao
from advisor import CareerAdvisor


def safe_input(mensagem: str, default: str = "") -> str:
    try:
        return input(mensagem)
    except OSError:
        print(f"[AVISO] Entrada não disponível. Usando padrão: {default!r}")
        return default


def ler_int(mensagem: str, minimo: Optional[int] = None, maximo: Optional[int] = None) -> int:
    while True:
        valor_str = safe_input(mensagem, default="").strip()

        if not valor_str:
            if minimo is not None:
                print(f"[INFO] Usando valor mínimo padrão: {minimo}")
                return minimo
            print("[INFO] Usando valor padrão 0")
            return 0

        if not valor_str.isdigit():
            print("Por favor, digite apenas números inteiros.")
            continue

        valor = int(valor_str)
        if minimo is not None and valor < minimo:
            print(f"O valor mínimo é {minimo}.")
            continue
        if maximo is not None and valor > maximo:
            print(f"O valor máximo é {maximo}.")
            continue
        return valor


def mostrar_cabecalho(titulo: str) -> None:
    print("\n" + "=" * 60)
    print(titulo)
    print("=" * 60)


def cadastrar_perfil(competencias_base: Dict[str, Competencia]) -> Perfil:
    mostrar_cabecalho("Cadastro de novo perfil")

    # Leitura e validação do nome
    while True:
        nome = safe_input("Seu nome: ", "Perfil sem nome").strip()

        if not nome:
            print("O nome não pode ser vazio. Tente novamente.")
            continue

        # Remove espaços e verifica se sobrou só número
        if nome.replace(" ", "").isdigit():
            print("O nome não pode ser composto apenas por números. Tente novamente.")
            continue

        break

    # Leitura e validação simples do objetivo
    objetivo = safe_input(
        "Seu objetivo profissional ou área de interesse: ",
        "Não especificado",
    ).strip() or "Não especificado"

    print("\nAgora, avalie suas competências em uma escala de 0 a 10.")
    print("0 = não tenho experiência; 10 = especialista que pode ensinar outras pessoas.\n")

    competencias_perfil: Dict[str, Competencia] = {}

    for comp_padrao in competencias_base.values():
        while True:
            nivel = ler_int(
                f"Nível em {comp_padrao.nome} ({comp_padrao.descricao}) [0-10]: ",
                0,
                10,
            )
            nova_comp = Competencia(
                nome=comp_padrao.nome,
                categoria=comp_padrao.categoria,
                descricao=comp_padrao.descricao,
                nivel=nivel,
            )
            competencias_perfil[nova_comp.nome.lower()] = nova_comp
            break

    perfil = Perfil(nome=nome, objetivo=objetivo, competencias=competencias_perfil)
    print("\nPerfil cadastrado com sucesso!")
    return perfil

def listar_perfis(perfis: List[Perfil]) -> None:
    mostrar_cabecalho("Perfis cadastrados")
    if not perfis:
        print("Nenhum perfil cadastrado ainda.")
        return

    for idx, perfil in enumerate(perfis, start=1):
        print(f"[{idx}] {perfil.nome} - Objetivo: {perfil.objetivo}")


def escolher_perfil(perfis: List[Perfil]) -> Optional[Perfil]:
    if not perfis:
        print("\nNenhum perfil disponível. Cadastre um perfil primeiro.")
        return None

    listar_perfis(perfis)
    indice = ler_int("\nEscolha o número do perfil: ", 1, len(perfis))
    return perfis[indice - 1]


def exibir_carreiras(carreiras: List[Carreira]) -> None:
    mostrar_cabecalho("Catálogo de carreiras do futuro")
    for idx, carreira in enumerate(carreiras, start=1):
        print(f"[{idx}] {carreira.nome}")
        print(f"    Descrição: {carreira.descricao}")
        print("    Competências-chave:")
        for nome_comp, peso in carreira.competencias_relevantes.items():
            print(f"        - {nome_comp.title()} (peso {peso:.2f})")
        print()


def analisar_perfil(perfil: Perfil, advisor: CareerAdvisor) -> None:
    mostrar_cabecalho(f"Análise de perfil - {perfil.nome}")
    print(f"Objetivo profissional: {perfil.objetivo}\n")

    print("Níveis de competências:")
    for comp in perfil.competencias.values():
        print(f"- {comp.nome} ({comp.categoria}): {comp.nivel}/10")

    print("\nGerando recomendações personalizadas...")
    recomendacoes = advisor.recomendar(perfil, top_n=3)

    if not recomendacoes:
        print("Não foi possível gerar recomendações.")
        return

    for idx, (carreira, score, gaps) in enumerate(recomendacoes, start=1):
        print("\n" + "-" * 60)
        print(f"Recomendação #{idx}: {carreira.nome}")
        print(f"Compatibilidade geral: {score:.2f}%")
        print(f"Descrição: {carreira.descricao}\n")

        fortes = [n for n, g in gaps.items() if g <= 3]
        desenvolver = [n for n, g in gaps.items() if g > 3]

        print("Pontos fortes para esta carreira:")
        if fortes:
            for nome in fortes:
                print(f"  [OK] {nome.title()} (nível atual: {perfil.obter_nivel(nome)}/10)")
        else:
            print("  (nenhuma competência em nível avançado ainda)")

        print("\nCompetências que valem reforçar:")
        if desenvolver:
            for nome in desenvolver:
                print(f"  - {nome.title()} (nível atual: {perfil.obter_nivel(nome)}/10)")
        else:
            print("  Você já está muito bem alinhado a esta carreira!")

        print("\nSugestões de trilhas de aprendizado:")
        for trilha in carreira.trilhas_aprendizado:
            print(f"  - {trilha}")


def teste_rapido() -> None:
    competencias = criar_competencias_padrao()
    competencias["lógica"].nivel = 8
    competencias["pensamento computacional"].nivel = 9
    competencias["dados e análise"].nivel = 7
    competencias["ética digital"].nivel = 6
    competencias["comunicação"].nivel = 6

    perfil_teste = Perfil(
        nome="Perfil de Teste",
        objetivo="Trabalhar com IA e análise de dados",
        competencias=competencias,
    )

    advisor = CareerAdvisor(criar_carreiras_padrao())
    recomendacoes = advisor.recomendar(perfil_teste)

    print("\n=== Teste rápido do motor de recomendação ===")
    for carreira, score, _ in recomendacoes:
        print(f"Carreira: {carreira.nome} | Score: {score}%")


def menu_principal() -> None:
    competencias_base = criar_competencias_padrao()
    carreiras = criar_carreiras_padrao()
    advisor = CareerAdvisor(carreiras)
    perfis: List[Perfil] = []

    while True:
        mostrar_cabecalho("Future Skills Lab - Orientador de Carreira")
        print("1 - Cadastrar novo perfil")
        print("2 - Listar perfis cadastrados")
        print("3 - Analisar perfil e gerar recomendações")
        print("4 - Ver catálogo de carreiras do futuro")
        print("0 - Sair")

        opcao = ler_int("\nEscolha uma opção: ", 0, 4)

        if opcao == 1:
            perfil = cadastrar_perfil(competencias_base)
            perfis.append(perfil)
            safe_input("\nPressione ENTER para voltar ao menu...", default="")
        elif opcao == 2:
            listar_perfis(perfis)
            safe_input("\nPressione ENTER para voltar ao menu...", default="")
        elif opcao == 3:
            perfil_escolhido = escolher_perfil(perfis)
            if perfil_escolhido:
                analisar_perfil(perfil_escolhido, advisor)
            safe_input("\nPressione ENTER para voltar ao menu...", default="")
        elif opcao == 4:
            exibir_carreiras(carreiras)
            safe_input("Pressione ENTER para voltar ao menu...", default="")
        elif opcao == 0:
            print("\nObrigado por usar o Future Skills Lab. Até a próxima!")
            break
