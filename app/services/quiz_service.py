from typing import List, Dict, Any, Optional
from app.models.quiz import Pergunta, Quiz
from app.data.perguntas import obter_perguntas, obter_categorias_disponiveis, obter_dificuldades_disponiveis, obter_estatisticas_perguntas
from app.services.ranking_service import ranking_service
import random


class QuizService:
    def __init__(self):
        self.quizes_ativos = {}
        self.quiz_info = {}  # Armazenar informações do quiz (categoria, dificuldade)

    def iniciar_quiz(self, usuario_id: str, categoria: Optional[str] = None, dificuldade: Optional[str] = None) -> Dict[str, Any]:
        """Inicia um novo quiz com perguntas manuais"""

        # Valores padrão
        categoria = categoria or "geral"
        dificuldade = dificuldade or "easy"

        print(f"Categoria: {categoria}, Dificuldade: {dificuldade}")

        # Determinar quantidade de perguntas baseada na dificuldade
        match dificuldade:
            case "easy":
                quantidade_perguntas = 10
            case "medium":
                quantidade_perguntas = 15
            case "hard":
                quantidade_perguntas = 20
            case _:
                quantidade_perguntas = 10

        # Buscar perguntas do banco manual
        perguntas_db = obter_perguntas(categoria, dificuldade, quantidade_perguntas)
        
        
        if not perguntas_db:
            return {
                "sucesso": False,
                "erro": f"Não há perguntas disponíveis para categoria '{categoria}' e dificuldade '{dificuldade}'"
            }

        quiz = Quiz(perguntas_db)
        self.quizes_ativos[usuario_id] = quiz
        self.quiz_info[usuario_id] = {
            'categoria': categoria,
            'dificuldade': dificuldade
        }

        return {
            "sucesso": True,
            "quiz_id": usuario_id,
            "total_perguntas": len(perguntas_db),
            "pergunta_atual": 1,
            "pergunta": perguntas_db[0].to_dict() if perguntas_db else None,
            "categoria": categoria,
            "dificuldade": dificuldade
        }

    def responder_pergunta(self, usuario_id: str, resposta: int) -> Dict[str, Any]:
        """Processa a resposta do usuário"""
        if usuario_id not in self.quizes_ativos:
            return {'sucesso': False, 'erro': 'Quiz não encontrado'}

        quiz = self.quizes_ativos[usuario_id]
        correta = quiz.responder_pergunta(resposta)

        proxima_pergunta = quiz.proxima_pergunta()

        if proxima_pergunta:
            return {
                'sucesso': True,
                'resposta_correta': correta,
                'proxima_pergunta': proxima_pergunta.to_dict(),
                'pergunta_atual': quiz.pergunta_atual + 1,
                'total_perguntas': len(quiz.perguntas),
                'pontuacao_atual': quiz.pontuacao
            }
        else:
            # Quiz finalizado
            resultados = quiz.finalizar_quiz()
            
            # Salvar resultado no ranking
            try:
                quiz_info = self.quiz_info.get(usuario_id, {})
                ranking_service.salvar_resultado(
                    usuario_id=int(usuario_id),
                    pontuacao=resultados['pontuacao'],
                    total_perguntas=resultados['total_perguntas'],
                    categoria=quiz_info.get('categoria', 'geral'),
                    dificuldade=quiz_info.get('dificuldade', 'easy'),
                    tempo_gasto=0  # TODO: Implementar cronômetro
                )
            except Exception as e:
                print(f"Erro ao salvar resultado: {e}")
            
            # Limpar dados do quiz
            del self.quizes_ativos[usuario_id]
            if usuario_id in self.quiz_info:
                del self.quiz_info[usuario_id]

            return {
                'sucesso': True,
                'quiz_finalizado': True,
                'resultados': resultados
            }

    def obter_pergunta_atual(self, usuario_id: str) -> Dict[str, Any]:
        """Retorna a pergunta atual do quiz do usuário"""
        if usuario_id not in self.quizes_ativos:
            return {'sucesso': False, 'erro': 'Quiz não encontrado'}

        quiz = self.quizes_ativos[usuario_id]
        pergunta_atual = quiz.proxima_pergunta()

        if pergunta_atual:
            return {
                'sucesso': True,
                'pergunta': pergunta_atual.to_dict(),
                'pergunta_atual': quiz.pergunta_atual + 1,
                'total_perguntas': len(quiz.perguntas)
            }
        else:
            return {'sucesso': False, 'erro': 'Quiz já finalizado'}

    def cancelar_quiz(self, usuario_id: str) -> Dict[str, Any]:
        """Cancela o quiz ativo do usuário"""
        if usuario_id in self.quizes_ativos:
            del self.quizes_ativos[usuario_id]
            if usuario_id in self.quiz_info:
                del self.quiz_info[usuario_id]
            return {'sucesso': True, 'mensagem': 'Quiz cancelado com sucesso'}
        return {'sucesso': False, 'erro': 'Nenhum quiz ativo encontrado'}

    def obter_categorias(self) -> Dict[str, Any]:
        """Retorna as categorias disponíveis"""
        categorias = obter_categorias_disponiveis()
        return {
            'sucesso': True,
            'categorias': categorias
        }

    def obter_dificuldades(self, categoria: str = "geral") -> Dict[str, Any]:
        """Retorna as dificuldades disponíveis para uma categoria"""
        dificuldades = obter_dificuldades_disponiveis(categoria)
        return {
            'sucesso': True,
            'categoria': categoria,
            'dificuldades': dificuldades
        }

    def obter_estatisticas(self) -> Dict[str, Any]:
        """Retorna estatísticas sobre as perguntas disponíveis"""
        estatisticas = obter_estatisticas_perguntas()
        return {
            'sucesso': True,
            'estatisticas': estatisticas
        }


quiz_service = QuizService()
