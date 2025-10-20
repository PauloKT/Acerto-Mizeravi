from datetime import datetime
from typing import List, Dict, Any

class Pergunta:
    def __init__(self, id: int, pergunta: str, opcoes: List[str], resposta_correta: int, categoria: str = "geral"):
        self.id = id
        self.pergunta = pergunta
        self.opcoes = opcoes  # Lista de opções de resposta
        self.resposta_correta = resposta_correta  # Índice da resposta correta (0-3)
        self.categoria = categoria
        self.data_criacao = datetime.utcnow()
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'pergunta': self.pergunta,
            'opcoes': self.opcoes,
            'resposta_correta': self.resposta_correta,
            'categoria': self.categoria,
            'data_criacao': self.data_criacao.isoformat()
        }
    
    def verificar_resposta(self, resposta_usuario: int) -> bool:
        """Verifica se a resposta do usuário está correta"""
        return resposta_usuario == self.resposta_correta

class Quiz:
    def __init__(self, perguntas: List[Pergunta]):
        self.perguntas = perguntas
        self.perguntas_sorteadas = []
        self.respostas_usuario = []
        self.pontuacao = 0
        self.pergunta_atual = 0
    
    def sortear_perguntas(self, quantidade: int = 10) -> List[Pergunta]:
        """Sorteia uma quantidade específica de perguntas aleatoriamente"""
        import random
        self.perguntas_sorteadas = random.sample(self.perguntas, min(quantidade, len(self.perguntas)))
        self.pergunta_atual = 0
        return self.perguntas_sorteadas
    
    def responder_pergunta(self, resposta: int) -> bool:
        """Registra a resposta do usuário e retorna se está correta"""
        if self.pergunta_atual < len(self.perguntas_sorteadas):
            pergunta = self.perguntas_sorteadas[self.pergunta_atual]
            correta = pergunta.verificar_resposta(resposta)
            self.respostas_usuario.append({
                'pergunta_id': pergunta.id,
                'resposta_usuario': resposta,
                'correta': correta
            })
            if correta:
                self.pontuacao += 1
            self.pergunta_atual += 1
            return correta
        return False
    
    def proxima_pergunta(self) -> Pergunta:
        """Retorna a próxima pergunta do quiz"""
        if self.pergunta_atual < len(self.perguntas_sorteadas):
            return self.perguntas_sorteadas[self.pergunta_atual]
        return None
    
    def finalizar_quiz(self) -> Dict[str, Any]:
        """Finaliza o quiz e retorna os resultados"""
        total_perguntas = len(self.perguntas_sorteadas)
        porcentagem = (self.pontuacao / total_perguntas * 100) if total_perguntas > 0 else 0
        
        return {
            'pontuacao': self.pontuacao,
            'total_perguntas': total_perguntas,
            'porcentagem': round(porcentagem, 2),
            'respostas': self.respostas_usuario
        }
