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
    print("📚 Sistema de Quiz disponível em: http://localhost:5000/quiz")
    print("🎮 Menu principal em: http://localhost:5000/menu")
    print("🔐 Login em: http://localhost:5000/")
    print("📝 Registro em: http://localhost:5000/register")
    
    # Verificar se há banco de dados disponível
    try:
        from config.database import get_db_connection
        print("✅ Modo: Banco de dados MySQL")
    except ImportError:
        print("⚠️  Modo: Sistema em memória (sem banco de dados)")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
