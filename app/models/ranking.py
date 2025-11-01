"""
Modelo para resultados de quiz e ranking
"""
from datetime import datetime
from typing import Dict, Any, List, Optional

class ResultadoQuiz:
    def __init__(self, id: int, usuario_id: int, pontuacao: int, total_perguntas: int, 
                 categoria: str, dificuldade: str, tempo_gasto: Optional[int] = None, 
                 data_realizacao: datetime = None):
        self.id = id
        self.usuario_id = usuario_id
        self.pontuacao = pontuacao
        self.total_perguntas = total_perguntas
        self.categoria = categoria
        self.dificuldade = dificuldade
        self.tempo_gasto = tempo_gasto or 0
        self.data_realizacao = data_realizacao or datetime.utcnow()
        self.porcentagem = round((pontuacao / total_perguntas * 100), 2) if total_perguntas > 0 else 0
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'usuario_id': self.usuario_id,
            'pontuacao': self.pontuacao,
            'total_perguntas': self.total_perguntas,
            'porcentagem': self.porcentagem,
            'categoria': self.categoria,
            'dificuldade': self.dificuldade,
            'tempo_gasto': self.tempo_gasto,
            'data_realizacao': self.data_realizacao.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ResultadoQuiz':
        return cls(
            id=data['id'],
            usuario_id=data['usuario_id'],
            pontuacao=data['pontuacao'],
            total_perguntas=data['total_perguntas'],
            categoria=data['categoria'],
            dificuldade=data['dificuldade'],
            tempo_gasto=data.get('tempo_gasto', 0),
            data_realizacao=data.get('data_realizacao', datetime.utcnow())
        )

class RankingEntry:
    def __init__(self, usuario_id: int, nome_usuario: str, pontuacao_total: int, 
                 total_quizes: int, melhor_pontuacao: int, categoria_preferida: str):
        self.usuario_id = usuario_id
        self.nome_usuario = nome_usuario
        self.pontuacao_total = pontuacao_total
        self.total_quizes = total_quizes
        self.melhor_pontuacao = melhor_pontuacao
        self.categoria_preferida = categoria_preferida
        self.media_pontuacao = round(pontuacao_total / total_quizes, 2) if total_quizes > 0 else 0
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'usuario_id': self.usuario_id,
            'nome_usuario': self.nome_usuario,
            'pontuacao_total': self.pontuacao_total,
            'total_quizes': self.total_quizes,
            'melhor_pontuacao': self.melhor_pontuacao,
            'categoria_preferida': self.categoria_preferida,
            'media_pontuacao': self.media_pontuacao
        }
