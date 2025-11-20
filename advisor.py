from typing import Dict, List, Tuple
from models import Perfil, Carreira


class CareerAdvisor:
    """Responsável por analisar perfis e gerar recomendações."""

    def __init__(self, carreiras: List[Carreira]):
        self.carreiras = carreiras

    def avaliar_compatibilidade(self, perfil: Perfil, carreira: Carreira) -> Tuple[float, Dict[str, int]]:
        soma_pesos = 0.0
        soma_niveis_ponderados = 0.0
        gaps: Dict[str, int] = {}

        for nome_comp, peso in carreira.competencias_relevantes.items():
            soma_pesos += peso
            nivel_usuario = perfil.obter_nivel(nome_comp)
            soma_niveis_ponderados += nivel_usuario * peso
            gaps[nome_comp] = max(0, 10 - nivel_usuario)

        if soma_pesos == 0:
            return 0.0, gaps

        score = (soma_niveis_ponderados / (10 * soma_pesos)) * 100
        return round(score, 2), gaps

    def recomendar(self, perfil: Perfil, top_n: int = 3):
        resultados = []
        for carreira in self.carreiras:
            score, gaps = self.avaliar_compatibilidade(perfil, carreira)
            resultados.append((carreira, score, gaps))
        resultados.sort(key=lambda x: x[1], reverse=True)
        return resultados[:top_n]
