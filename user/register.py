from flask import Blueprint, request, jsonify
from datetime import datetime
try:
    from config.database import get_db
    DB_AVAILABLE = True
except ImportError:
    DB_AVAILABLE = False

api = Blueprint('api', __name__)

usuarios_db = []
proximo_id = 1

class Usuario:
    def __init__(self, nome, email):
        global proximo_id
        self.id = proximo_id
        proximo_id += 1
        self.nome = nome
        self.email = email
        self.data_registro = datetime.utcnow()
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'data_registro': self.data_registro.isoformat()
        }

def validar_dados(data):
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

def buscar_usuario_por_nome(nome):
    for usuario in usuarios_db:
        if usuario.nome == nome:
            return usuario
    return None

@api.route('/api/registrar', methods=['POST'])
def registrar_usuario():
    data = request.get_json()
    erros = validar_dados(data)
    if erros:
        return jsonify({'sucesso': False, 'erros': erros}), 400

    if DB_AVAILABLE:
        try:
            db = get_db()
            cursor = db.cursor(dictionary=True)
            
            cursor.execute("SELECT * FROM usuarios WHERE email = %s", (data['email'].strip(),))
            usuario_existente = cursor.fetchone()
            if usuario_existente:
                cursor.close()
                db.close()
                return jsonify({'sucesso': False, 'erro': 'Este email já está registrado.'}), 409

            cursor.execute(
                "INSERT INTO usuarios (nome, email, data_registro) VALUES (%s, %s, %s)",
                (data['nome'].strip(), data['email'].strip(), datetime.utcnow())
            )
            db.commit()
            cursor.close()
            db.close()
            return jsonify({'sucesso': True, 'mensagem': 'Usuário registrado com sucesso!'}), 201
        except Exception as e:
            print(f"Erro no banco de dados: {e}")
            # Fallback para sistema em memória
            pass
    
    # Sistema em memória (fallback)
    email = data['email'].strip()
    nome = data['nome'].strip()
    
    # Verificar se já existe
    for usuario in usuarios_db:
        if usuario.email == email:
            return jsonify({'sucesso': False, 'erro': 'Este email já está registrado.'}), 409
    
    # Criar novo usuário
    novo_usuario = Usuario(nome, email)
    usuarios_db.append(novo_usuario)
    
    return jsonify({'sucesso': True, 'mensagem': 'Usuário registrado com sucesso!'}), 201

@api.route('/api/login', methods=['POST'])
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

@api.route('/api/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify({
        'sucesso': True,
        'usuarios': [usuario.to_dict() for usuario in usuarios_db],
        'total': len(usuarios_db)
    })

@api.route('/api/usuarios/<int:usuario_id>', methods=['GET'])
def buscar_usuario(usuario_id):
    usuario = next((u for u in usuarios_db if u.id == usuario_id), None)
    if not usuario:
        return jsonify({'sucesso': False, 'erro': 'Usuário não encontrado'}), 404
    return jsonify({'sucesso': True, 'usuario': usuario.to_dict()})

@api.route('/api/usuarios/<int:usuario_id>', methods=['PUT'])
def atualizar_usuario(usuario_id):
    usuario = next((u for u in usuarios_db if u.id == usuario_id), None)
    if not usuario:
        return jsonify({'sucesso': False, 'erro': 'Usuário não encontrado'}), 404
    data = request.get_json()
    erros = validar_dados(data)
    if erros:
        return jsonify({'sucesso': False, 'erros': erros}), 400
    usuario.nome = data['nome'].strip()
    usuario.email = data['email'].strip()
    return jsonify({
        'sucesso': True,
        'mensagem': 'Usuário atualizado com sucesso!',
        'usuario': usuario.to_dict()
    })

@api.route('/api/usuarios/<int:usuario_id>', methods=['DELETE'])
def deletar_usuario(usuario_id):
    usuario = next((u for u in usuarios_db if u.id == usuario_id), None)
    if not usuario:
        return jsonify({'sucesso': False, 'erro': 'Usuário não encontrado'}), 404
    usuarios_db.remove(usuario)
    return jsonify({'sucesso': True, 'mensagem': 'Usuário deletado com sucesso!'})