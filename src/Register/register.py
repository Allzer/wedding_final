from flask import Blueprint, render_template, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from src.Register.update import update

reg = Blueprint('reg', __name__, template_folder='templates', static_folder='static')

@reg.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form = request.form
        print(form)
        if len(form['psw']) >= 3 and len(form['s_n']) >= 3 \
        and len(form['first_name']) >= 3 and len(form['last_name']) >= 3 and len(form['patronymic']) >= 3 \
        and len(form['p_number']) >= 11:
            hash = generate_password_hash(form['psw'])
            check_password_hash(hash, form['ag_psw'])
            if check_password_hash(hash, form['ag_psw']):
                update(form)
                flash('Вы успешно зарегистрировались')
            else:
                flash('Пароли не совпадают')
        else:
            flash('Введите данные корректно')

    return render_template('reg.html', title="Регистрация")










