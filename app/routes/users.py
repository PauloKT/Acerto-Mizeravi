from flask import Blueprint, request, jsonify
from app.services.user_service import UserService

users_bp = Blueprint('users', __name__)

@users_bp.route('/api/usuarios', methods=['GET'])
def listar_usuarios():
    try:
        usuarios = UserService.get_all_users()
        return jsonify({
            'sucesso': True,
            'usuarios': [usuario.to_dict() for usuario in usuarios],
            'total': len(usuarios)
        })
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': 'Erro interno do servidor'}), 500

@users_bp.route('/api/usuarios/<int:usuario_id>', methods=['GET'])
def buscar_usuario(usuario_id):
    try:
        usuario = UserService.get_user_by_id(usuario_id)
        if not usuario:
            return jsonify({'sucesso': False, 'erro': 'Usuário não encontrado'}), 404
        
        return jsonify({'sucesso': True, 'usuario': usuario.to_dict()})
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': 'Erro interno do servidor'}), 500

@users_bp.route('/api/usuarios/<int:usuario_id>', methods=['PUT'])
def atualizar_usuario(usuario_id):
    try:
        data = request.get_json()
        erros = []
        nome = data.get('nome', '').strip()
        email = data.get('email', '').strip()
        
        if not nome:
            erros.append('Nome é obrigatório')
        if not email:
            erros.append('Email é obrigatório')
        elif '@' not in email or '.' not in email:
            erros.append('Email inválido')
        
        if erros:
            return jsonify({'sucesso': False, 'erros': erros}), 400

        usuario = UserService.update_user(usuario_id, nome, email)
        
        return jsonify({
            'sucesso': True,
            'mensagem': 'Usuário atualizado com sucesso!',
            'usuario': usuario.to_dict()
        })
    except ValueError as e:
        return jsonify({'sucesso': False, 'erro': str(e)}), 404
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': 'Erro interno do servidor'}), 500

@users_bp.route('/api/usuarios/<int:usuario_id>', methods=['DELETE'])
def deletar_usuario(usuario_id):
    try:
        UserService.delete_user(usuario_id)
        return jsonify({'sucesso': True, 'mensagem': 'Usuário deletado com sucesso!'})
    except ValueError as e:
        return jsonify({'sucesso': False, 'erro': str(e)}), 404
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': 'Erro interno do servidor'}), 500