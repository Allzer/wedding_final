from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash
from database import db
from src.guests.model import Guests
from src.user import User

auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        p_number = request.form.get('p_number')
        password = request.form.get('psw')
        guest = db.session.query(Guests).filter_by(p_number=p_number).first()

        if guest and check_password_hash(guest.password, password):
            user = User(guest)
            rm = True if request.form.get('remainme') else False
            login_user(user, remember=rm)
            return redirect(url_for('main.index'))
        else:
            error = 'Неверный номер телефона или пароль'
            flash(error, 'error')
    return render_template('login.html', title='Авторизация', error=error)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Вы вышли из системы', 'success')
    return redirect(url_for('auth.login'))
