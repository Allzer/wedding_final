from flask import Flask, render_template, request, redirect, flash, url_for, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_migrate import Migrate
from werkzeug.security import check_password_hash
from config import SECRET_KEY, DATABASE_URL
from database import db
from src.Guests.model import Guests
from src.Register.register import reg

app = Flask(__name__)
app.secret_key = SECRET_KEY

app.register_blueprint(reg, url_prefix='/registrations')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, guest):
        self.name = guest.first_name
        self.last_name = guest.last_name
        self.id = guest.id
        self.p_number = guest.p_number
        self.password = guest.password
        self.active = True
    @property
    def is_active(self):
        return self.active

@login_manager.user_loader
def load_user(user_id):
    guest = db.session.get(Guests, int(user_id))
    if guest:
        return User(guest)
    return None

@app.route("/index")
@app.route("/")
@login_required
def index():
    return render_template('index.html', title='Главная страница')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        p_number = request.form.get('p_number')
        password = request.form.get('psw')
        guest = db.session.query(Guests).filter_by(p_number=p_number).first()

        if guest and check_password_hash(guest.password, password):
            user = User(guest)
            rm = True if request.form.get('remainme') else False
            login_user(user, remember=rm)

            return redirect(url_for('index'))
        else:
            flash('Неверный номер телефона или пароль', 'error')
            print('Неверный номер телефона или пароль')
            return redirect(url_for('login'))
    return render_template("login.html", title='Авторизация')

@app.route('/profile')
@login_required
def profile():
    name = current_user.name
    last_name = current_user.last_name
    return render_template('profile.html', title='Профиль', name=name, l_name=last_name)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Вы вышли из системы', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
