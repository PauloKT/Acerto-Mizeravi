from flask import Flask, send_from_directory
from app.routes.auth import auth_bp
from app.routes.users import users_bp

app = Flask(__name__, static_folder="static")
app.register_blueprint(auth_bp)
app.register_blueprint(users_bp)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/register')
def register():
    return send_from_directory(app.static_folder, 'register.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(debug=True)