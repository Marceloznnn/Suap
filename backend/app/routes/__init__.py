from .login import bp as home
from .esqueci_senha import bp as esqueci_senha

def init_app(app):
    app.register_blueprint(home)
    app.register_blueprint(esqueci_senha)
