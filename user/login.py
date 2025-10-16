from flask import Blueprint, request, jsonify
from user.register import usuarios_db

login_api = Blueprint('login_api', __name__)

def buscar_usuario_por_nome(nome):
    for usuario in usuarios_db:
        if usuario.nome == nome:
            return usuario
    return None

@login_api.route('/api/login', methods=['POST'])
def login_usuario():
    data = request.get_json()
    nome = data.get('nome', '').strip()
    if not nome:
        return jsonify({'sucesso': False, 'erro': 'Nome é obrigatório'}), 400
    usuario = buscar_usuario_por_nome(nome)
    if usuario:
        return jsonify({'sucesso': True, 'mensagem': 'Login realizado!', 'usuario': usuario.to_dict()})
    else:
        return jsonify({'sucesso': False, 'erro': 'Usuário não encontrado'}), 404