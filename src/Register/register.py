from flask import Blueprint, render_template

reg = Blueprint('reg', __name__, template_folder='templates', static_folder='static')

@reg.route('/')
def index():
    return render_template('reg.html', title="Регистрация")
 





