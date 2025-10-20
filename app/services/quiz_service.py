from typing import List, Dict, Any, Optional
from app.models.quiz import Pergunta, Quiz
import random

class QuizService:
    def __init__(self):
        self.perguntas_db = self._carregar_perguntas_padrao()
        self.quizes_ativos = {}  # Armazena quizes ativos por usuário
    
    def _carregar_perguntas_padrao(self) -> List[Pergunta]:
        """Carrega um conjunto padrão de perguntas de conhecimentos gerais"""
        perguntas = [
            Pergunta(
                id=1,
                pergunta="Qual é a capital do Brasil?",
                opcoes=["São Paulo", "Rio de Janeiro", "Brasília", "Salvador"],
                resposta_correta=2,
                categoria="geografia"
            ),
            Pergunta(
                id=2,
                pergunta="Quem escreveu 'Dom Casmurro'?",
                opcoes=["Machado de Assis", "José de Alencar", "Castro Alves", "Graciliano Ramos"],
                resposta_correta=0,
                categoria="literatura"
            ),
            Pergunta(
                id=3,
                pergunta="Qual é o maior planeta do sistema solar?",
                opcoes=["Terra", "Júpiter", "Saturno", "Netuno"],
                resposta_correta=1,
                categoria="ciencia"
            ),
            Pergunta(
                id=4,
                pergunta="Em que ano o Brasil foi descoberto?",
                opcoes=["1498", "1500", "1502", "1504"],
                resposta_correta=1,
                categoria="historia"
            ),
            Pergunta(
                id=5,
                pergunta="Qual é a fórmula química da água?",
                opcoes=["H2O", "CO2", "NaCl", "O2"],
                resposta_correta=0,
                categoria="ciencia"
            ),
            Pergunta(
                id=6,
                pergunta="Qual é o nome do processo de transformação da água em vapor?",
                opcoes=["Condensação", "Evaporação", "Solidificação", "Fusão"],
                resposta_correta=1,
                categoria="ciencia"
            ),
            Pergunta(
                id=7,
                pergunta="Quem pintou a 'Mona Lisa'?",
                opcoes=["Van Gogh", "Picasso", "Leonardo da Vinci", "Michelangelo"],
                resposta_correta=2,
                categoria="arte"
            ),
            Pergunta(
                id=8,
                pergunta="Qual é o maior oceano do mundo?",
                opcoes=["Atlântico", "Índico", "Pacífico", "Ártico"],
                resposta_correta=2,
                categoria="geografia"
            ),
            Pergunta(
                id=9,
                pergunta="Em que continente fica o Egito?",
                opcoes=["Ásia", "África", "Europa", "América"],
                resposta_correta=1,
                categoria="geografia"
            ),
            Pergunta(
                id=10,
                pergunta="Qual é a velocidade da luz no vácuo?",
                opcoes=["300.000 km/s", "150.000 km/s", "450.000 km/s", "600.000 km/s"],
                resposta_correta=0,
                categoria="ciencia"
            ),
            Pergunta(
                id=11,
                pergunta="Quem foi o primeiro presidente do Brasil?",
                opcoes=["Getúlio Vargas", "Juscelino Kubitschek", "Deodoro da Fonseca", "Prudente de Morais"],
                resposta_correta=2,
                categoria="historia"
            ),
            Pergunta(
                id=12,
                pergunta="Qual é o nome do processo de fotossíntese?",
                opcoes=["Respiração", "Digestão", "Fotossíntese", "Circulação"],
                resposta_correta=2,
                categoria="ciencia"
            ),
            Pergunta(
                id=13,
                pergunta="Qual é a moeda oficial do Japão?",
                opcoes=["Won", "Yuan", "Yen", "Dong"],
                resposta_correta=2,
                categoria="geografia"
            ),
            Pergunta(
                id=14,
                pergunta="Quem escreveu 'Os Lusíadas'?",
                opcoes=["Fernando Pessoa", "Luís de Camões", "Eça de Queirós", "José Saramago"],
                resposta_correta=1,
                categoria="literatura"
            ),
            Pergunta(
                id=15,
                pergunta="Qual é o elemento químico com símbolo 'Au'?",
                opcoes=["Prata", "Ouro", "Alumínio", "Cobre"],
                resposta_correta=1,
                categoria="ciencia"
            ),
            Pergunta(
                id=16,
                pergunta="Em que país fica a Torre Eiffel?",
                opcoes=["Itália", "França", "Espanha", "Alemanha"],
                resposta_correta=1,
                categoria="geografia"
            ),
            Pergunta(
                id=17,
                pergunta="Qual é o nome do processo de divisão celular?",
                opcoes=["Mitose", "Meiose", "Fotossíntese", "Respiração"],
                resposta_correta=0,
                categoria="ciencia"
            ),
            Pergunta(
                id=18,
                pergunta="Quem foi o compositor de 'A Quinta Sinfonia'?",
                opcoes=["Mozart", "Bach", "Beethoven", "Chopin"],
                resposta_correta=2,
                categoria="arte"
            ),
            Pergunta(
                id=19,
                pergunta="Qual é o nome do maior deserto do mundo?",
                opcoes=["Saara", "Gobi", "Antártico", "Atacama"],
                resposta_correta=0,
                categoria="geografia"
            ),
            Pergunta(
                id=20,
                pergunta="Em que século viveu Leonardo da Vinci?",
                opcoes=["XIV", "XV", "XVI", "XVII"],
                resposta_correta=1,
                categoria="historia"
            )
        ]
        return perguntas
    
    def iniciar_quiz(self, usuario_id: str, quantidade_perguntas: int = 10) -> Dict[str, Any]:
        """Inicia um novo quiz para o usuário"""
        quiz = Quiz(self.perguntas_db)
        perguntas_sorteadas = quiz.sortear_perguntas(quantidade_perguntas)
        
        self.quizes_ativos[usuario_id] = quiz
        
        return {
            'sucesso': True,
            'quiz_id': usuario_id,
            'total_perguntas': len(perguntas_sorteadas),
            'pergunta_atual': 1,
            'pergunta': perguntas_sorteadas[0].to_dict()
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
                'pontuacao_atual': quiz.pontuacao
            }
        else:
            # Quiz finalizado
            resultados = quiz.finalizar_quiz()
            del self.quizes_ativos[usuario_id]
            
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
                'total_perguntas': len(quiz.perguntas_sorteadas)
            }
        else:
            return {'sucesso': False, 'erro': 'Quiz já finalizado'}
    
    def cancelar_quiz(self, usuario_id: str) -> Dict[str, Any]:
        """Cancela o quiz ativo do usuário"""
        if usuario_id in self.quizes_ativos:
            del self.quizes_ativos[usuario_id]
            return {'sucesso': True, 'mensagem': 'Quiz cancelado com sucesso'}
        return {'sucesso': False, 'erro': 'Nenhum quiz ativo encontrado'}
    
    def obter_perguntas_por_categoria(self, categoria: str) -> List[Dict[str, Any]]:
        """Retorna todas as perguntas de uma categoria específica"""
        perguntas_categoria = [p for p in self.perguntas_db if p.categoria == categoria]
        return [p.to_dict() for p in perguntas_categoria]
    
    def obter_todas_perguntas(self) -> List[Dict[str, Any]]:
        """Retorna todas as perguntas disponíveis"""
        return [p.to_dict() for p in self.perguntas_db]
    
    def adicionar_pergunta(self, pergunta: str, opcoes: List[str], resposta_correta: int, categoria: str = "geral") -> Dict[str, Any]:
        """Adiciona uma nova pergunta ao banco de dados"""
        novo_id = max([p.id for p in self.perguntas_db]) + 1 if self.perguntas_db else 1
        nova_pergunta = Pergunta(novo_id, pergunta, opcoes, resposta_correta, categoria)
        self.perguntas_db.append(nova_pergunta)
        return {'sucesso': True, 'pergunta': nova_pergunta.to_dict()}

# Instância global do serviço
quiz_service = QuizService()
