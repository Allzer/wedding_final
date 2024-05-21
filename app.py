from flask import Flask, render_template, request, redirect, flash, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
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
        self.id = guest.id
        self.p_number = guest.p_number
        self.password = guest.password
        self.active = True

    @property
    def is_active(self):
        return self.active

@login_manager.user_loader
def load_user(user_id):
    guest = Guests.query.get(int(user_id))
    if guest:
        return User(guest)
    return None

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html', title='Главная страница')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        p_number = request.form.get('p_number')
        password = request.form.get('psw')
        guest = Guests.query.filter_by(p_number=p_number).first()

        if guest and check_password_hash(guest.password, password):
            user = User(guest)
            login_user(user)
            flash('Успешный вход', 'success')
            return redirect(url_for('index'))
        else:
            flash('Неверный номер телефона или пароль', 'danger')
            return redirect(url_for('login'))

    return render_template("login.html", title='Авторизация')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Вы вышли из системы', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
