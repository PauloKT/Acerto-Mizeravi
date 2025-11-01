from flask import Blueprint, request, jsonify
from app.services.quiz_service import quiz_service

quiz_api = Blueprint('quiz_api', __name__)

@quiz_api.route('/api/quiz/iniciar', methods=['POST'])
def iniciar_quiz():
    """Inicia um novo quiz"""
    try:
        data = request.get_json()
        usuario_id = data.get('usuario_id')
        categoria = data.get('categoria')
        dificuldade = data.get('dificuldade')
        
        if not usuario_id:
            return jsonify({'sucesso': False, 'erro': 'ID do usuário é obrigatório'}), 400
        
        resultado = quiz_service.iniciar_quiz(usuario_id, categoria, dificuldade)
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

@quiz_api.route('/api/quiz/categorias', methods=['GET'])
def obter_categorias():
    """Retorna as categorias disponíveis"""
    try:
        resultado = quiz_service.obter_categorias()
        return jsonify(resultado)
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': f'Erro interno: {str(e)}'}), 500

@quiz_api.route('/api/quiz/dificuldades', methods=['GET'])
def obter_dificuldades():
    """Retorna as dificuldades disponíveis para uma categoria"""
    try:
        categoria = request.args.get('categoria', 'geral')
        resultado = quiz_service.obter_dificuldades(categoria)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': f'Erro interno: {str(e)}'}), 500

@quiz_api.route('/api/quiz/estatisticas', methods=['GET'])
def obter_estatisticas():
    """Retorna estatísticas sobre as perguntas disponíveis"""
    try:
        resultado = quiz_service.obter_estatisticas()
        return jsonify(resultado)
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': f'Erro interno: {str(e)}'}), 500