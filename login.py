from flask import Flask, request, jsonify, g
from datetime import datetime, timedelta
import os
import jwt
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Armazenamento em memória (simulando banco de dados)
usuarios_db = []
proximo_id = 1

# =====================
# Autenticação (in-memory)
# =====================

# Estruturas em memória para contas de autenticação e tokens de refresh
auth_users_db_by_email = {}
auth_users_db_by_id = {}
proximo_auth_id = 1

# Mapear jti do refresh -> user_id
active_refresh_tokens = {}
# Mapear user_id -> set(jtis)
user_refresh_tokens = {}

# Configurações JWT
ACCESS_TOKEN_EXPIRES_MINUTES = 15
REFRESH_TOKEN_EXPIRES_DAYS = 7
JWT_ALGORITHM = 'HS256'

try:
    # Evita erro se não existir chave explícita
    app.config['SECRET_KEY'] = os.environ.get('JWT_SECRET', 'dev-secret-change-me')
except Exception:
    # Fallback defensivo
    app.config['SECRET_KEY'] = 'dev-secret-change-me'


class AuthUser:
    def __init__(self, email, password_hash, nome=None):
        global proximo_auth_id
        self.id = proximo_auth_id
        proximo_auth_id += 1
        self.email = email
        self.password_hash = password_hash
        self.nome = (nome or '').strip() or None
        self.data_criacao = datetime.utcnow()

    def to_public_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'nome': self.nome,
            'data_criacao': self.data_criacao.isoformat()
        }


def _jwt_now():
    return datetime.utcnow()


def _issue_token(user, token_type):
    now = _jwt_now()
    if token_type == 'access':
        exp = now + timedelta(minutes=ACCESS_TOKEN_EXPIRES_MINUTES)
    elif token_type == 'refresh':
        exp = now + timedelta(days=REFRESH_TOKEN_EXPIRES_DAYS)
    else:
        raise ValueError('Tipo de token inválido')

    jti = str(uuid.uuid4())
    payload = {
        'sub': user.id,
        'email': user.email,
        'type': token_type,
        'jti': jti,
        'iat': int(now.timestamp()),
        'exp': int(exp.timestamp()),
    }

    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm=JWT_ALGORITHM)

    if token_type == 'refresh':
        active_refresh_tokens[jti] = user.id
        if user.id not in user_refresh_tokens:
            user_refresh_tokens[user.id] = set()
        user_refresh_tokens[user.id].add(jti)

    return token


def _decode_token(token, expected_type):
    payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=[JWT_ALGORITHM])
    if payload.get('type') != expected_type:
        raise jwt.InvalidTokenError('Tipo de token inválido')
    return payload


def _issue_token_pair(user):
    access = _issue_token(user, 'access')
    refresh = _issue_token(user, 'refresh')
    return {'access': access, 'refresh': refresh}


def _revoke_refresh_jti(jti):
    user_id = active_refresh_tokens.pop(jti, None)
    if user_id is not None and user_id in user_refresh_tokens:
        user_refresh_tokens[user_id].discard(jti)


def _revoke_all_refresh_for_user(user_id):
    jtis = list(user_refresh_tokens.get(user_id, set()))
    for jti in jtis:
        _revoke_refresh_jti(jti)

# Classe para representar usuários (sem dependência de banco)
class Usuario:
    def __init__(self, nome, curso):
        global proximo_id
        self.id = proximo_id
        proximo_id += 1
        self.nome = nome
        self.curso = curso
        self.data_registro = datetime.utcnow()
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'curso': self.curso,
            'data_registro': self.data_registro.isoformat()
        }
    
    @staticmethod
    def buscar_por_id(usuario_id):
        for usuario in usuarios_db:
            if usuario.id == usuario_id:
                return usuario
        return None


# =====================
# Endpoints de Autenticação
# =====================

def _validate_email(email):
    if not email or '@' not in email:
        return False
    if len(email.strip()) < 6:
        return False
    return True


def _validate_password(password):
    return bool(password) and len(password) >= 6


@app.route('/api/auth/register', methods=['POST'])
def auth_register():
    try:
        data = request.get_json() or {}
        email = (data.get('email') or '').strip().lower()
        nome = (data.get('nome') or data.get('name') or '').strip()
        senha = data.get('senha') if 'senha' in data else data.get('password')

        erros = []
        if not _validate_email(email):
            erros.append('Email inválido')
        if not _validate_password(senha):
            erros.append('Senha deve ter pelo menos 6 caracteres')
        if email in auth_users_db_by_email:
            erros.append('Email já registrado')

        if erros:
            return jsonify({'sucesso': False, 'erros': erros}), 400

        password_hash = generate_password_hash(senha)
        user = AuthUser(email=email, password_hash=password_hash, nome=nome)
        auth_users_db_by_email[email] = user
        auth_users_db_by_id[user.id] = user

        tokens = _issue_token_pair(user)
        return jsonify({
            'sucesso': True,
            'mensagem': 'Usuário registrado com sucesso!'
            , 'usuario': user.to_public_dict(),
            'tokens': tokens
        }), 201
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': 'Erro ao registrar', 'detalhes': str(e)}), 500


@app.route('/api/auth/login', methods=['POST'])
def auth_login():
    try:
        data = request.get_json() or {}
        email = (data.get('email') or '').strip().lower()
        senha = data.get('senha') if 'senha' in data else data.get('password')

        if not _validate_email(email) or not _validate_password(senha):
            return jsonify({'sucesso': False, 'erro': 'Credenciais inválidas'}), 400

        user = auth_users_db_by_email.get(email)
        if not user:
            return jsonify({'sucesso': False, 'erro': 'Email ou senha incorretos'}), 401

        check = check_password_hash(user.password_hash, senha)
        if not check:
            return jsonify({'sucesso': False, 'erro': 'Email ou senha incorretos'}), 401

        tokens = _issue_token_pair(user)
        return jsonify({'sucesso': True, 'mensagem': 'Login realizado com sucesso!', 'usuario': user.to_public_dict(), 'tokens': tokens})
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': 'Erro ao fazer login', 'detalhes': str(e)}), 500


@app.route('/api/auth/refresh', methods=['POST'])
def auth_refresh():
    try:
        data = request.get_json() or {}
        refresh_token = data.get('refresh_token')
        if not refresh_token:
            return jsonify({'sucesso': False, 'erro': 'refresh_token é obrigatório'}), 400

        payload = _decode_token(refresh_token, 'refresh')
        jti = payload.get('jti')
        user_id = payload.get('sub')

        if jti not in active_refresh_tokens or active_refresh_tokens.get(jti) != user_id:
            return jsonify({'sucesso': False, 'erro': 'refresh_token inválido ou revogado'}), 401

        # Rotaciona o refresh: revoga o atual e emite novo par
        _revoke_refresh_jti(jti)
        user = auth_users_db_by_id.get(user_id)
        if not user:
            return jsonify({'sucesso': False, 'erro': 'Usuário não encontrado'}), 404

        tokens = _issue_token_pair(user)
        return jsonify({'sucesso': True, 'tokens': tokens})
    except jwt.ExpiredSignatureError:
        return jsonify({'sucesso': False, 'erro': 'refresh_token expirado'}), 401
    except jwt.InvalidTokenError as e:
        return jsonify({'sucesso': False, 'erro': 'refresh_token inválido', 'detalhes': str(e)}), 401
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': 'Erro ao renovar token', 'detalhes': str(e)}), 500


@app.route('/api/auth/logout', methods=['POST'])
def auth_logout():
    try:
        data = request.get_json() or {}
        refresh_token = data.get('refresh_token')
        todas_sessoes = bool(data.get('todas_sessoes') or data.get('all'))

        if not refresh_token:
            return jsonify({'sucesso': False, 'erro': 'refresh_token é obrigatório'}), 400

        payload = _decode_token(refresh_token, 'refresh')
        user_id = payload.get('sub')
        jti = payload.get('jti')

        if todas_sessoes:
            _revoke_all_refresh_for_user(user_id)
        else:
            if jti not in active_refresh_tokens:
                return jsonify({'sucesso': False, 'erro': 'refresh_token inválido ou já revogado'}), 400
            _revoke_refresh_jti(jti)

        return jsonify({'sucesso': True, 'mensagem': 'Logout realizado com sucesso'})
    except jwt.InvalidTokenError as e:
        return jsonify({'sucesso': False, 'erro': 'refresh_token inválido', 'detalhes': str(e)}), 401
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': 'Erro ao realizar logout', 'detalhes': str(e)}), 500


def require_auth(view_func):
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization', '')
        if not auth_header.startswith('Bearer '):
            return jsonify({'sucesso': False, 'erro': 'Token ausente'}), 401
        token = auth_header.split(' ', 1)[1]
        try:
            payload = _decode_token(token, 'access')
            user_id = payload.get('sub')
            user = auth_users_db_by_id.get(user_id)
            if not user:
                return jsonify({'sucesso': False, 'erro': 'Usuário não encontrado'}), 404
            g.current_user = user
        except jwt.ExpiredSignatureError:
            return jsonify({'sucesso': False, 'erro': 'Token expirado'}), 401
        except jwt.InvalidTokenError as e:
            return jsonify({'sucesso': False, 'erro': 'Token inválido', 'detalhes': str(e)}), 401
        return view_func(*args, **kwargs)
    wrapper.__name__ = view_func.__name__
    return wrapper


@app.route('/api/auth/me', methods=['GET'])
@require_auth
def auth_me():
    user = g.current_user
    return jsonify({'sucesso': True, 'usuario': user.to_public_dict()})


@app.route('/api/auth/change-password', methods=['POST'])
@require_auth
def auth_change_password():
    try:
        data = request.get_json() or {}
        atual = data.get('senha_atual') if 'senha_atual' in data else data.get('current_password')
        nova = data.get('nova_senha') if 'nova_senha' in data else data.get('new_password')

        if not _validate_password(atual) or not _validate_password(nova):
            return jsonify({'sucesso': False, 'erro': 'Senha inválida'}), 400

        user = g.current_user
        check = check_password_hash(user.password_hash, atual)
        if not check:
            return jsonify({'sucesso': False, 'erro': 'Senha atual incorreta'}), 401

        user.password_hash = generate_password_hash(nova)
        _revoke_all_refresh_for_user(user.id)
        return jsonify({'sucesso': True, 'mensagem': 'Senha alterada com sucesso'})
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': 'Erro ao alterar senha', 'detalhes': str(e)}), 500

# Função para validar dados de entrada
def validar_dados(data):
    erros = []
    
    if not data.get('nome'):
        erros.append('Nome é obrigatório')
    elif len(data['nome'].strip()) < 2:
        erros.append('Nome deve ter pelo menos 2 caracteres')
    
    if not data.get('curso'):
        erros.append('Curso é obrigatório')
    elif len(data['curso'].strip()) < 2:
        erros.append('Curso deve ter pelo menos 2 caracteres')
    
    return erros

# Endpoint para registrar usuário
@app.route('/api/registrar', methods=['POST'])
def registrar_usuario():
    try:
        data = request.get_json()
        
        # Validar dados
        erros = validar_dados(data)
        if erros:
            return jsonify({
                'sucesso': False,
                'erros': erros
            }), 400
        
        # Criar novo usuário
        novo_usuario = Usuario(
            nome=data['nome'].strip(),
            curso=data['curso'].strip()
        )
        
        # Adicionar à lista em memória
        usuarios_db.append(novo_usuario)
        
        return jsonify({
            'sucesso': True,
            'mensagem': 'Usuário registrado com sucesso!',
            'usuario': novo_usuario.to_dict()
        }), 201
        
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'erro': 'Erro interno do servidor',
            'detalhes': str(e)
        }), 500

# Endpoint para listar todos os usuários
@app.route('/api/usuarios', methods=['GET'])
def listar_usuarios():
    try:
        return jsonify({
            'sucesso': True,
            'usuarios': [usuario.to_dict() for usuario in usuarios_db],
            'total': len(usuarios_db)
        })
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'erro': 'Erro ao buscar usuários',
            'detalhes': str(e)
        }), 500

# Endpoint para buscar usuário por ID
@app.route('/api/usuarios/<int:usuario_id>', methods=['GET'])
def buscar_usuario(usuario_id):
    try:
        usuario = Usuario.buscar_por_id(usuario_id)
        if not usuario:
            return jsonify({
                'sucesso': False,
                'erro': 'Usuário não encontrado'
            }), 404
        
        return jsonify({
            'sucesso': True,
            'usuario': usuario.to_dict()
        })
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'erro': 'Erro ao buscar usuário',
            'detalhes': str(e)
        }), 500

# Endpoint para atualizar usuário
@app.route('/api/usuarios/<int:usuario_id>', methods=['PUT'])
def atualizar_usuario(usuario_id):
    try:
        usuario = Usuario.buscar_por_id(usuario_id)
        if not usuario:
            return jsonify({
                'sucesso': False,
                'erro': 'Usuário não encontrado'
            }), 404
        
        data = request.get_json()
        
        # Validar dados
        erros = validar_dados(data)
        if erros:
            return jsonify({
                'sucesso': False,
                'erros': erros
            }), 400
        
        # Atualizar dados
        usuario.nome = data['nome'].strip()
        usuario.curso = data['curso'].strip()
        
        return jsonify({
            'sucesso': True,
            'mensagem': 'Usuário atualizado com sucesso!',
            'usuario': usuario.to_dict()
        })
        
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'erro': 'Erro ao atualizar usuário',
            'detalhes': str(e)
        }), 500

# Endpoint para deletar usuário
@app.route('/api/usuarios/<int:usuario_id>', methods=['DELETE'])
def deletar_usuario(usuario_id):
    try:
        usuario = Usuario.buscar_por_id(usuario_id)
        if not usuario:
            return jsonify({
                'sucesso': False,
                'erro': 'Usuário não encontrado'
            }), 404
        
        usuarios_db.remove(usuario)
        
        return jsonify({
            'sucesso': True,
            'mensagem': 'Usuário deletado com sucesso!'
        })
        
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'erro': 'Erro ao deletar usuário',
            'detalhes': str(e)
        }), 500

# Endpoint de teste
@app.route('/api/teste', methods=['GET'])
def teste():
    return jsonify({
        'mensagem': 'API de registro de usuários e autenticação funcionando!',
        'endpoints': {
            'POST /api/registrar': 'Registrar novo usuário',
            'GET /api/usuarios': 'Listar todos os usuários',
            'GET /api/usuarios/<id>': 'Buscar usuário por ID',
            'PUT /api/usuarios/<id>': 'Atualizar usuário',
            'DELETE /api/usuarios/<id>': 'Deletar usuário',
            'POST /api/auth/register': 'Registrar conta (email/senha) e obter tokens',
            'POST /api/auth/login': 'Login com email/senha e obter tokens',
            'POST /api/auth/refresh': 'Renovar par de tokens (usa refresh)',
            'POST /api/auth/logout': 'Logout (revoga refresh atual ou todos)',
            'GET /api/auth/me': 'Obter dados do usuário autenticado (Bearer access)',
            'POST /api/auth/change-password': 'Trocar senha (requer Bearer access)'
        }
    })

if __name__ == '__main__':
    print("🚀 Servidor iniciado!")
    print("📝 Dados armazenados em memória (serão perdidos ao reiniciar)")
    print("🔗 API disponível em: http://localhost:5000")
    print("📋 Endpoints disponíveis:")
    print("   POST /api/registrar - Registrar usuário")
    print("   GET  /api/usuarios - Listar usuários")
    print("   GET  /api/usuarios/{id} - Buscar usuário")
    print("   PUT  /api/usuarios/{id} - Atualizar usuário")
    print("   DELETE /api/usuarios/{id} - Deletar usuário")
    print("   GET  /api/teste - Testar API")
    print("   POST /api/auth/register - Registrar conta (email/senha)")
    print("   POST /api/auth/login - Login com email/senha")
    print("   POST /api/auth/refresh - Renovar tokens (refresh)")
    print("   POST /api/auth/logout - Logout (revoga refresh)")
    print("   GET  /api/auth/me - Dados do usuário autenticado")
    print("   POST /api/auth/change-password - Trocar senha autenticado")
    print("\n💡 Para integração futura com banco de dados:")
    print("   - Substitua a lista 'usuarios_db' por operações de banco")
    print("   - Mantenha a mesma estrutura da classe Usuario")
    print("   - Os endpoints permanecem os mesmos")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
