from flask import Blueprint, render_template, request, flash, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from src.register.update import update
from database import db
from src.guests.model import Guests

reg = Blueprint('reg', __name__, template_folder='templates', static_folder='static')

@reg.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form = request.form

        if len(form['psw']) < 3 or len(form['s_n']) < 3 \
            or len(form['first_name']) < 3 or len(form['last_name']) < 3 or len(form['patronymic']) < 3 \
            or len(form['p_number']) < 11:
            error = 'Введите данные корректно'
            flash(error,'error')
            return render_template('reg.html', title="Регистрация", error=error)

        existing_p_number = db.session.query(Guests).filter_by(p_number=form['p_number']).first()
        existing_s_n = db.session.query(Guests).filter_by(s_n=form['s_n']).first()

        if existing_s_n:
            error='Этот VK или Telegram уже зарегистрирован'
            flash(error,'error')
            return render_template('reg.html', title="Регистрация", error=error)

        if existing_p_number:
            error='Этот номер телефона уже зарегистрирован'
            flash(error,'error')
            return render_template('reg.html', title="Регистрация", error=error)
        
        if form['psw'] != form['ag_psw']:
            error = 'Пароли не совпадают'
            flash(error,'error')
            return render_template('reg.html', title="Регистрация", error=error)

        update(form)

        return redirect('/auth/login', code=302, Response=None)

    return render_template('reg.html', title="Регистрация")
