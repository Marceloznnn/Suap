from flask import Blueprint, render_template, request

bp = Blueprint('esqueci_senha', __name__)

@bp.route('/esqueci-senha', methods=['GET', 'POST'])
def esqueci_senha():
    message = None
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        if email.lower() != 'estagio@gmail.com':
            message = 'E-mail inválido.'
        else:
            message = 'E-mail enviado com sucesso.'
    return render_template('esqueci_senha.html', message=message)
