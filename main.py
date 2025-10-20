from flask import Flask, send_from_directory
from user.register import api
from user.login import login_api
from app.routes.quiz import quiz_api

app = Flask(__name__, static_folder="static")

# Configurações básicas
app.config['SECRET_KEY'] = 'dev-secret-key'
app.config['DEBUG'] = True

# Registrar blueprints
app.register_blueprint(api)
app.register_blueprint(login_api)
app.register_blueprint(quiz_api)

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
    print("🚀 Iniciando Show do Tabareli...")
    print("📚 Sistema de Quiz disponível em: http://localhost:5000/quiz")
    print("🎮 Menu principal em: http://localhost:5000/menu")
    print("⚠️  Modo desenvolvimento - sem banco de dados")
    app.run(debug=True, host='0.0.0.0', port=5000)
