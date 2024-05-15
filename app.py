from flask import Flask, render_template, url_for, request, flash
from flask_migrate import Migrate
from werkzeug.security import check_password_hash

from config import SECRET_KEY, DATABASE_URL
from database import db
from src.Guests.model import Guests

from src.Register.register import reg

app = Flask(__name__)
app.secret_key = SECRET_KEY

app.register_blueprint(reg, url_prefix='/registrations')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html', title='Главная страница')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form = request.form
        number = db.session.query(Guests.p_number).filter(Guests.p_number==form['p_number']).first()
        psw = db.session.query(Guests.password).filter(Guests.password==form['psw']).first()
        print(psw)
        print(number)


        if check_password_hash(form['psw'],psw) and form['p_number'] == number:
            print("Авторизовался!")
        else:
            err = 'Неверный пароль'
    return render_template("login.html", title='Авторизация', msg=err)

if __name__ == '__main__':
    app.run(debug=True)