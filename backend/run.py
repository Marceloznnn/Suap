import os
from flask import Flask
from app.routes import init_app

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'app', 'templates')

app = Flask(__name__, template_folder=TEMPLATE_DIR)
app.secret_key = 'estagio-2025'

init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
