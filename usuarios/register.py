from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# Armazenamento em memória (simulando banco de dados)
usuarios_db = []
proximo_id = 1

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
        'mensagem': 'API de registro de usuários funcionando!',
        'endpoints': {
            'POST /api/registrar': 'Registrar novo usuário',
            'GET /api/usuarios': 'Listar todos os usuários',
            'GET /api/usuarios/<id>': 'Buscar usuário por ID',
            'PUT /api/usuarios/<id>': 'Atualizar usuário',
            'DELETE /api/usuarios/<id>': 'Deletar usuário'
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
    print("\n💡 Para integração futura com banco de dados:")
    print("   - Substitua a lista 'usuarios_db' por operações de banco")
    print("   - Mantenha a mesma estrutura da classe Usuario")
    print("   - Os endpoints permanecem os mesmos")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
