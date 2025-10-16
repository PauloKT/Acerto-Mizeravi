from flask import Blueprint, request, jsonify
from datetime import datetime
from config.database import get_db

user_api = Blueprint('user_api', __name__)

def validar_dados(data):
    erros = []
    if not data:
        erros.append('Requisição JSON inválida')
        return erros
    nome = data.get('nome', '').strip()
    email = data.get('email', '').strip()
    if not nome:
        erros.append('Nome é obrigatório')
    if not email:
        erros.append('Email é obrigatório')
    elif '@' not in email or '.' not in email:
        erros.append('Email inválido')
    return erros

@user_api.route('/api/registrar', methods=['POST'])
def registrar_usuario():
    data = request.get_json()
    erros = validar_dados(data)
    if erros:
        return jsonify({'sucesso': False, 'erros': erros}), 400

    nome = data['nome'].strip()
    email = data['email'].strip()
    db = get_db()
    cursor = db.cursor(dictionary=True)
    try:
        cursor.execute("SELECT id FROM usuarios WHERE email = %s", (email,))
        if cursor.fetchone():
            return jsonify({'sucesso': False, 'erro': 'Este email já está registrado.'}), 409

        cursor.execute(
            "INSERT INTO usuarios (nome, email, data_registro) VALUES (%s, %s, %s)",
            (nome, email, datetime.utcnow())
        )
        db.commit()
        user_id = cursor.lastrowid

        cursor.execute("SELECT id, nome, email, data_registro FROM usuarios WHERE id = %s", (user_id,))
        usuario = cursor.fetchone()
    except Exception as e:
        db.rollback()
        return jsonify({'sucesso': False, 'erro': 'Erro ao registrar usuário.', 'detalhes': str(e)}), 500
    finally:
        cursor.close()
        db.close()

    # normaliza data_registro para isoformat se necessário
    if usuario and 'data_registro' in usuario and hasattr(usuario['data_registro'], 'isoformat'):
        usuario['data_registro'] = usuario['data_registro'].isoformat()

    return jsonify({'sucesso': True, 'mensagem': 'Usuário registrado com sucesso!', 'usuario': usuario}), 201

@user_api.route('/api/usuarios', methods=['GET'])
def listar_usuarios():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    try:
        cursor.execute("SELECT id, nome, email, data_registro FROM usuarios")
        usuarios = cursor.fetchall()
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': 'Erro ao listar usuários.', 'detalhes': str(e)}), 500
    finally:
        cursor.close()
        db.close()

    for u in usuarios:
        if 'data_registro' in u and hasattr(u['data_registro'], 'isoformat'):
            u['data_registro'] = u['data_registro'].isoformat()

    return jsonify({'sucesso': True, 'usuarios': usuarios, 'total': len(usuarios)})

@user_api.route('/api/usuarios/<int:usuario_id>', methods=['GET'])
def buscar_usuario(usuario_id):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    try:
        cursor.execute("SELECT id, nome, email, data_registro FROM usuarios WHERE id = %s", (usuario_id,))
        usuario = cursor.fetchone()
        if not usuario:
            return jsonify({'sucesso': False, 'erro': 'Usuário não encontrado'}), 404
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': 'Erro ao buscar usuário.', 'detalhes': str(e)}), 500
    finally:
        cursor.close()
        db.close()

    if 'data_registro' in usuario and hasattr(usuario['data_registro'], 'isoformat'):
        usuario['data_registro'] = usuario['data_registro'].isoformat()

    return jsonify({'sucesso': True, 'usuario': usuario})

@user_api.route('/api/usuarios/<int:usuario_id>', methods=['PUT'])
def atualizar_usuario(usuario_id):
    data = request.get_json()
    erros = validar_dados(data)
    if erros:
        return jsonify({'sucesso': False, 'erros': erros}), 400

    nome = data['nome'].strip()
    email = data['email'].strip()

    db = get_db()
    cursor = db.cursor(dictionary=True)
    try:
        # verifica existência
        cursor.execute("SELECT id FROM usuarios WHERE id = %s", (usuario_id,))
        if not cursor.fetchone():
            return jsonify({'sucesso': False, 'erro': 'Usuário não encontrado'}), 404

        # checa unicidade do email (exceto este usuário)
        cursor.execute("SELECT id FROM usuarios WHERE email = %s AND id <> %s", (email, usuario_id))
        if cursor.fetchone():
            return jsonify({'sucesso': False, 'erro': 'Email já em uso por outro usuário.'}), 409

        cursor.execute(
            "UPDATE usuarios SET nome = %s, email = %s WHERE id = %s",
            (nome, email, usuario_id)
        )
        db.commit()

        cursor.execute("SELECT id, nome, email, data_registro FROM usuarios WHERE id = %s", (usuario_id,))
        usuario = cursor.fetchone()
    except Exception as e:
        db.rollback()
        return jsonify({'sucesso': False, 'erro': 'Erro ao atualizar usuário.', 'detalhes': str(e)}), 500
    finally:
        cursor.close()
        db.close()

    if usuario and 'data_registro' in usuario and hasattr(usuario['data_registro'], 'isoformat'):
        usuario['data_registro'] = usuario['data_registro'].isoformat()

    return jsonify({'sucesso': True, 'mensagem': 'Usuário atualizado com sucesso!', 'usuario': usuario})

@user_api.route('/api/usuarios/<int:usuario_id>', methods=['DELETE'])
def deletar_usuario(usuario_id):
    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT id FROM usuarios WHERE id = %s", (usuario_id,))
        if not cursor.fetchone():
            return jsonify({'sucesso': False, 'erro': 'Usuário não encontrado'}), 404

        cursor.execute("DELETE FROM usuarios WHERE id = %s", (usuario_id,))
        db.commit()
    except Exception as e:
        db.rollback()