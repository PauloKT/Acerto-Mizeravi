from flask import Flask, send_from_directory
from user.register import api
from user.login import login_api

app = Flask(__name__, static_folder="static")
app.register_blueprint(api)
app.register_blueprint(login_api)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/register')
def register_page():
    return send_from_directory(app.static_folder, 'register.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(debug=True)