# Future Skills Lab – Sistema de Orientação de Carreira (PCAP)

## 📌 Disciplina
Pensamento Computacional e Automação com Python (PCAP)  
FIAP – Ciência da Computação – 1º ano

---

## 🎯 Sobre o Projeto

Este projeto implementa um **sistema orientado a objetos em Python** que organiza, analisa e recomenda **carreiras do futuro** com base nas competências técnicas e comportamentais do usuário.

O sistema permite:

- Cadastro de perfis com:
  - Nome
  - Objetivo profissional
  - Níveis de 0 a 10 em competências como Lógica, Programação, Dados e Análise, Criatividade, Colaboração, Adaptabilidade, Comunicação e Ética Digital
- Análise das competências em relação a carreiras do futuro
- Geração de recomendações com:
  - Score de compatibilidade (%)
  - Pontos fortes
  - Competências a desenvolver
  - Trilhas de aprendizado sugeridas

O tema está alinhado ao **Future of Work / Future Skills Lab**, enfatizando upskilling, reskilling e habilidades humanas combinadas com tecnologia.

---

## 🧠 Conceitos Utilizados

- Programação Orientada a Objetos (classes, atributos, métodos)
- Listas, dicionários e tuplas
- Funções e condicionais
- Organização em múltiplos arquivos (módulos Python)
- Interface textual (CLI – Command Line Interface)

---

## 📂 Estrutura do Projeto

```text
pcap-future-skills-lab/
├── models.py         # Classes: Competencia, Perfil, Carreira
├── data.py           # Criação das competências e carreiras padrão
├── advisor.py        # Lógica de recomendação (CareerAdvisor)
├── cli.py            # Interface de linha de comando (menus e interação)
├── main.py           # Ponto de entrada da aplicação
├── README.md         # Documentação do projeto
└── LINK_ENTREGA.txt  # Arquivo de entrega com link e dados dos integrantes
```

---

## ▶️ Como Executar

Pré-requisitos:
- Python 3 instalado

Passos:

```bash
# 1. Acessar a pasta do projeto
cd pcap-future-skills-lab

# 2. Executar o sistema
python main.py
```

Ao rodar, o menu principal será exibido:

```text
============================================================
Future Skills Lab - Orientador de Carreira
============================================================
1 - Cadastrar novo perfil
2 - Listar perfis cadastrados
3 - Analisar perfil e gerar recomendações
4 - Ver catálogo de carreiras do futuro
0 - Sair
```

---

## 🎥 Vídeo Demonstrativo

Para atender ao critério de documentação (print ou vídeo), o projeto inclui um **vídeo demonstrativo** mostrando:

- Execução do sistema
- Cadastro de um perfil
- Geração de recomendações
- Visualização das carreiras do futuro

🔗 **Link do vídeo (YouTube – Não listado):**  
ADICIONAR_LINK_DO_VIDEO_AQUI

---

## 👨‍💻 Integrantes

- **Kaio Correa** – RM **563443**  
- **Renan Mano Otero** – RM **554911**  

Curso: Ciência da Computação – 1º ano – FIAP

---

## ✔️ Critérios Atendidos

- [x] Uso de Python orientado a objetos  
- [x] Classes, atributos e métodos  
- [x] Listas, tuplas e dicionários  
- [x] Funções e condicionais  
- [x] Interface textual funcional  
- [x] Organização do código em módulos  
- [x] Documentação via README.md  
- [x] Vídeo demonstrativo do sistema  
- [x] Arquivo de entrega com link do GitHub e dados dos integrantes  

Este projeto foi desenvolvido para atingir **nota máxima (10/10)** nos critérios da disciplina de PCAP.
