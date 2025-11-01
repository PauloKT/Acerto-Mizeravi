from flask import Flask, send_from_directory
from app.routes.auth import auth_bp
from app.routes.users import users_bp
from app.routes.quiz import quiz_api
from app.routes.ranking import ranking_bp
from config.simple_config import config

app = Flask(__name__, static_folder="static")

# Configurações da aplicação
app.config.from_object(config['default'])

# Registrar blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(users_bp)
app.register_blueprint(quiz_api)
app.register_blueprint(ranking_bp)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'login.html')

@app.route('/menu')
def menu():
    return send_from_directory(app.static_folder, 'menu.html')

@app.route('/quiz')
def quiz_page():
    return send_from_directory(app.static_folder, 'quiz.html')

@app.route('/register')
def register_page():
    return send_from_directory(app.static_folder, 'register.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    print("🚀 Iniciando Sistema de Quiz...")
    print("=" * 50)
    
    # Verificar se há banco de dados disponível e inicializar
    try:
        from config.database import get_db_connection, initialize_database
        
        print("🗄️  Sistema configurado para rodar com BANCO DE DADOS MySQL")
        print("🔄 Inicializando banco de dados com schema atualizado...")
        
        # Inicializar banco de dados com o arquivo SQL (incluindo triggers)
        if initialize_database():
            print("✅ Schema do banco de dados atualizado com sucesso!")
            print("=" * 50)
            print("✅ Sistema rodando com BANCO DE DADOS ativo!")
        else:
            print("⚠️  Não foi possível inicializar o banco de dados automaticamente.")
            print("💡 Você pode executar o arquivo database_schema.sql manualmente no MySQL.")
            print("=" * 50)
            print("⚠️  Sistema iniciado, mas banco de dados não foi inicializado automaticamente.")
            
    except ImportError:
        print("⚠️  Modo: Sistema em memória (sem banco de dados)")
        print("=" * 50)
    except Exception as e:
        print(f"⚠️  Erro ao inicializar banco de dados: {e}")
        print("💡 Você pode executar o arquivo database_schema.sql manualmente no MySQL.")
        print("=" * 50)
        print("⚠️  Sistema iniciado, mas banco de dados não foi inicializado automaticamente.")
    
    print("📚 Sistema de Quiz disponível em: http://localhost:5000/quiz")
    print("🎮 Menu principal em: http://localhost:5000/menu")
    print("🔐 Login em: http://localhost:5000/")
    print("📝 Registro em: http://localhost:5000/register")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
