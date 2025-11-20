from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Competencia:
    """Representa uma competência (hard ou soft skill)."""

    nome: str
    categoria: str
    descricao: str
    nivel: int = 0

    def atualizar_nivel(self, novo_nivel: int) -> None:
        if 0 <= novo_nivel <= 10:
            self.nivel = novo_nivel
        else:
            raise ValueError("O nível deve estar entre 0 e 10.")


@dataclass
class Perfil:
    """Perfil profissional do usuário (ou de um candidato)."""

    nome: str
    objetivo: str
    competencias: Dict[str, Competencia] = field(default_factory=dict)

    def adicionar_competencia(self, comp: Competencia) -> None:
        self.competencias[comp.nome.lower()] = comp

    def obter_nivel(self, nome_competencia: str) -> int:
        comp = self.competencias.get(nome_competencia.lower())
        return comp.nivel if comp else 0


@dataclass
class Carreira:
    """Carreira ou trilha profissional do futuro."""

    nome: str
    descricao: str
    competencias_relevantes: Dict[str, float]
    nivel_minimo: int = 5
    trilhas_aprendizado: List[str] = field(default_factory=list)
