from flask import Blueprint, request, jsonify
from app.services.quiz_service import quiz_service

quiz_api = Blueprint('quiz_api', __name__)

@quiz_api.route('/api/quiz/iniciar', methods=['POST'])
def iniciar_quiz():
    """Inicia um novo quiz"""
    try:
        data = request.get_json()
        usuario_id = data.get('usuario_id')
        quantidade_perguntas = data.get('quantidade_perguntas', 10)
        
        if not usuario_id:
            return jsonify({'sucesso': False, 'erro': 'ID do usuário é obrigatório'}), 400
        
        if quantidade_perguntas < 1 or quantidade_perguntas > 20:
            return jsonify({'sucesso': False, 'erro': 'Quantidade de perguntas deve estar entre 1 e 20'}), 400
        
        resultado = quiz_service.iniciar_quiz(usuario_id, quantidade_perguntas)
        return jsonify(resultado)
        
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': f'Erro interno: {str(e)}'}), 500

@quiz_api.route('/api/quiz/responder', methods=['POST'])
def responder_pergunta():
    """Processa a resposta do usuário"""
    try:
        data = request.get_json()
        usuario_id = data.get('usuario_id')
        resposta = data.get('resposta')
        
        if not usuario_id:
            return jsonify({'sucesso': False, 'erro': 'ID do usuário é obrigatório'}), 400
        
        if resposta is None or resposta < 0 or resposta > 3:
            return jsonify({'sucesso': False, 'erro': 'Resposta deve ser um número entre 0 e 3'}), 400
        
        resultado = quiz_service.responder_pergunta(usuario_id, resposta)
        return jsonify(resultado)
        
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': f'Erro interno: {str(e)}'}), 500

@quiz_api.route('/api/quiz/pergunta-atual', methods=['GET'])
def obter_pergunta_atual():
    """Retorna a pergunta atual do quiz"""
    try:
        usuario_id = request.args.get('usuario_id')
        
        if not usuario_id:
            return jsonify({'sucesso': False, 'erro': 'ID do usuário é obrigatório'}), 400
        
        resultado = quiz_service.obter_pergunta_atual(usuario_id)
        return jsonify(resultado)
        
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': f'Erro interno: {str(e)}'}), 500

@quiz_api.route('/api/quiz/cancelar', methods=['POST'])
def cancelar_quiz():
    """Cancela o quiz ativo do usuário"""
    try:
        data = request.get_json()
        usuario_id = data.get('usuario_id')
        
        if not usuario_id:
            return jsonify({'sucesso': False, 'erro': 'ID do usuário é obrigatório'}), 400
        
        resultado = quiz_service.cancelar_quiz(usuario_id)
        return jsonify(resultado)
        
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': f'Erro interno: {str(e)}'}), 500

@quiz_api.route('/api/quiz/perguntas', methods=['GET'])
def obter_perguntas():
    """Retorna todas as perguntas ou perguntas de uma categoria específica"""
    try:
        categoria = request.args.get('categoria')
        
        if categoria:
            perguntas = quiz_service.obter_perguntas_por_categoria(categoria)
        else:
            perguntas = quiz_service.obter_todas_perguntas()
        
        return jsonify({
            'sucesso': True,
            'perguntas': perguntas,
            'total': len(perguntas)
        })
        
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': f'Erro interno: {str(e)}'}), 500

@quiz_api.route('/api/quiz/perguntas', methods=['POST'])
def adicionar_pergunta():
    """Adiciona uma nova pergunta ao banco de dados"""
    try:
        data = request.get_json()
        pergunta = data.get('pergunta')
        opcoes = data.get('opcoes')
        resposta_correta = data.get('resposta_correta')
        categoria = data.get('categoria', 'geral')
        
        # Validações
        if not pergunta:
            return jsonify({'sucesso': False, 'erro': 'Pergunta é obrigatória'}), 400
        
        if not opcoes or len(opcoes) != 4:
            return jsonify({'sucesso': False, 'erro': 'Deve haver exatamente 4 opções'}), 400
        
        if resposta_correta is None or resposta_correta < 0 or resposta_correta > 3:
            return jsonify({'sucesso': False, 'erro': 'Resposta correta deve ser um índice entre 0 e 3'}), 400
        
        resultado = quiz_service.adicionar_pergunta(pergunta, opcoes, resposta_correta, categoria)
        return jsonify(resultado)
        
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': f'Erro interno: {str(e)}'}), 500

@quiz_api.route('/api/quiz/categorias', methods=['GET'])
def obter_categorias():
    """Retorna todas as categorias disponíveis"""
    try:
        categorias = list(set([p.categoria for p in quiz_service.perguntas_db]))
        return jsonify({
            'sucesso': True,
            'categorias': categorias
        })
        
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': f'Erro interno: {str(e)}'}), 500
