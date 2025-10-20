#!/usr/bin/env python3
"""
Script de demonstração do sistema de quiz
Este script demonstra como usar o sistema de quiz criado
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.services.quiz_service import quiz_service

def demonstrar_quiz():
    """Demonstra o funcionamento do sistema de quiz"""
    print("🧠 Sistema de Quiz de Conhecimentos Gerais")
    print("=" * 50)
    
    # Mostrar todas as perguntas disponíveis
    print("\n📚 Perguntas disponíveis:")
    perguntas = quiz_service.obter_todas_perguntas()
    print(f"Total de perguntas: {len(perguntas)}")
    
    # Mostrar categorias
    categorias = list(set([p['categoria'] for p in perguntas]))
    print(f"Categorias: {', '.join(categorias)}")
    
    # Iniciar um quiz de demonstração
    print("\n🎯 Iniciando quiz de demonstração...")
    usuario_id = "demo_user"
    resultado_inicio = quiz_service.iniciar_quiz(usuario_id, 5)
    
    if resultado_inicio['sucesso']:
        print(f"✅ Quiz iniciado com {resultado_inicio['total_perguntas']} perguntas")
        
        # Simular respostas
        pontuacao = 0
        for i in range(resultado_inicio['total_perguntas']):
            pergunta_atual = quiz_service.obter_pergunta_atual(usuario_id)
            
            if pergunta_atual['sucesso']:
                pergunta = pergunta_atual['pergunta']
                print(f"\n❓ Pergunta {i+1}: {pergunta['pergunta']}")
                
                for j, opcao in enumerate(pergunta['opcoes']):
                    print(f"   {j}: {opcao}")
                
                # Simular resposta aleatória (para demonstração)
                import random
                resposta_simulada = random.randint(0, 3)
                print(f"🤖 Resposta simulada: {resposta_simulada}")
                
                resultado_resposta = quiz_service.responder_pergunta(usuario_id, resposta_simulada)
                
                if resultado_resposta['sucesso']:
                    if resultado_resposta['resposta_correta']:
                        print("✅ Resposta correta!")
                        pontuacao += 1
                    else:
                        print("❌ Resposta incorreta!")
                    
                    if resultado_resposta['quiz_finalizado']:
                        print("\n🏁 Quiz finalizado!")
                        resultados = resultado_resposta['resultados']
                        print(f"📊 Pontuação final: {resultados['pontuacao']}/{resultados['total_perguntas']}")
                        print(f"📈 Porcentagem: {resultados['porcentagem']}%")
                        break
            else:
                print("❌ Erro ao obter pergunta")
                break
    
    print("\n🎉 Demonstração concluída!")

def mostrar_estatisticas():
    """Mostra estatísticas das perguntas"""
    print("\n📊 Estatísticas das perguntas:")
    perguntas = quiz_service.obter_todas_perguntas()
    
    # Contar por categoria
    categorias = {}
    for pergunta in perguntas:
        cat = pergunta['categoria']
        categorias[cat] = categorias.get(cat, 0) + 1
    
    for categoria, quantidade in categorias.items():
        print(f"  {categoria}: {quantidade} perguntas")

if __name__ == "__main__":
    try:
        demonstrar_quiz()
        mostrar_estatisticas()
    except Exception as e:
        print(f"❌ Erro na demonstração: {e}")
        import traceback
        traceback.print_exc()
