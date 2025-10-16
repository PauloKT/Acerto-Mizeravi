from flask import Blueprint, request, jsonify
from app.services.user_service import UserService

auth_bp = Blueprint('auth', __name__)

def validar_dados_registro(data):
    erros = []
    nome = data.get('nome', '').strip()
    email = data.get('email', '').strip()
    
    if not nome:
        erros.append('Nome é obrigatório')
    if not email:
        erros.append('Email é obrigatório')
    elif '@' not in email or '.' not in email:
        erros.append('Email inválido')
    
    return erros

@auth_bp.route('/api/registrar', methods=['POST'])
def registrar_usuario():
    try:
        data = request.get_json()
        erros = validar_dados_registro(data)
        
        if erros:
            return jsonify({'sucesso': False, 'erros': erros}), 400

        usuario = UserService.create_user(data['nome'].strip(), data['email'].strip())
        
        return jsonify({
            'sucesso': True, 
            'mensagem': 'Usuário registrado com sucesso!',
            'usuario': usuario.to_dict()
        }), 201
        
    except ValueError as e:
        return jsonify({'sucesso': False, 'erro': str(e)}), 409
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': 'Erro interno do servidor'}), 500

@auth_bp.route('/api/login', methods=['POST'])
def login_usuario():
    try:
        data = request.get_json()
        nome = data.get('nome', '').strip()
        
        if not nome:
            return jsonify({'sucesso': False, 'erro': 'Nome é obrigatório'}), 400

        usuario = UserService.get_user_by_name(nome)
        
        if usuario:
            return jsonify({
                'sucesso': True, 
                'mensagem': 'Login realizado!', 
                'usuario': usuario.to_dict()
            })
        else:
            return jsonify({'sucesso': False, 'erro': 'Usuário não encontrado'}), 404
            
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': 'Erro interno do servidor'}), 500