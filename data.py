from typing import Dict, List
from models import Competencia, Carreira


def criar_competencias_padrao() -> Dict[str, Competencia]:
    """Cria um conjunto base de competências usadas no sistema."""

    competencias_base = [
        Competencia(
            nome="Lógica",
            categoria="técnica",
            descricao="Capacidade de resolver problemas de forma estruturada",
        ),
        Competencia(
            nome="Pensamento Computacional",
            categoria="técnica",
            descricao="Quebrar problemas em partes, reconhecer padrões e criar algoritmos",
        ),
        Competencia(
            nome="Programação",
            categoria="técnica",
            descricao="Conhecimentos básicos de código (como Python) para automatizar tarefas",
        ),
        Competencia(
            nome="Dados e Análise",
            categoria="técnica",
            descricao="Coletar, organizar e interpretar dados para tomada de decisão",
        ),
        Competencia(
            nome="Criatividade",
            categoria="comportamental",
            descricao="Gerar ideias novas, conectar conceitos e inovar",
        ),
        Competencia(
            nome="Colaboração",
            categoria="comportamental",
            descricao="Trabalhar bem em equipe, inclusive em ambientes remotos/híbridos",
        ),
        Competencia(
            nome="Adaptabilidade",
            categoria="comportamental",
            descricao="Aprender, desaprender e se ajustar a cenários em mudança",
        ),
        Competencia(
            nome="Comunicação",
            categoria="comportamental",
            descricao="Expressar ideias com clareza, de forma oral e escrita",
        ),
        Competencia(
            nome="Ética Digital",
            categoria="comportamental",
            descricao="Uso responsável de tecnologia, dados e IA",
        ),
    ]

    return {c.nome.lower(): c for c in competencias_base}


def criar_carreiras_padrao() -> List[Carreira]:
    """Cria uma lista de carreiras alinhadas ao tema Future at Work."""

    carreiras = [
        Carreira(
            nome="Curador de Inteligência Artificial",
            descricao=(
                "Profissional que seleciona, avalia e orienta o uso de modelos de IA "
                "em empresas, garantindo qualidade, ética e alinhamento ao negócio."
            ),
            competencias_relevantes={
                "lógica": 0.2,
                "pensamento computacional": 0.25,
                "dados e análise": 0.2,
                "ética digital": 0.2,
                "comunicação": 0.15,
            },
            nivel_minimo=6,
            trilhas_aprendizado=[
                "Fundamentos de Python e IA generativa",
                "Ética e viés em algoritmos",
                "Engenharia de prompt e avaliação de modelos",
            ],
        ),
        Carreira(
            nome="Designer de Experiências Imersivas",
            descricao=(
                "Cria experiências digitais em realidade virtual, aumentada e ambientes híbridos "
                "para educação, trabalho remoto e entretenimento."
            ),
            competencias_relevantes={
                "criatividade": 0.3,
                "colaboração": 0.15,
                "programação": 0.15,
                "pensamento computacional": 0.2,
                "comunicação": 0.2,
            },
            nivel_minimo=5,
            trilhas_aprendizado=[
                "Introdução a UX/UI para ambientes imersivos",
                "Ferramentas de criação 3D e engines de jogos",
                "Oficinas de storytelling e narrativa interativa",
            ],
        ),
        Carreira(
            nome="Engenheiro de Sustentabilidade Digital",
            descricao=(
                "Profissional que conecta tecnologia, dados e sustentabilidade para reduzir "
                "impactos ambientais e apoiar decisões responsáveis."
            ),
            competencias_relevantes={
                "dados e análise": 0.3,
                "lógica": 0.2,
                "ética digital": 0.2,
                "colaboração": 0.15,
                "adaptabilidade": 0.15,
            },
            nivel_minimo=6,
            trilhas_aprendizado=[
                "Fundamentos de ESG e ODS (ONU)",
                "Análise de dados aplicada à sustentabilidade",
                "Automação de relatórios e dashboards em Python",
            ],
        ),
        Carreira(
            nome="Facilitador de Comunidades de Aprendizagem",
            descricao=(
                "Organiza comunidades globais de aprendizado contínuo, conectando pessoas, "
                "projetos e trilhas de requalificação (upskilling e reskilling)."
            ),
            competencias_relevantes={
                "comunicação": 0.3,
                "colaboração": 0.25,
                "adaptabilidade": 0.2,
                "criatividade": 0.15,
                "ética digital": 0.1,
            },
            nivel_minimo=5,
            trilhas_aprendizado=[
                "Comunicação e facilitação em ambientes online",
                "Ferramentas digitais para comunidades globais",
                "Metodologias ativas e aprendizagem baseada em projetos",
            ],
        ),
    ]

    return carreiras
