from flask import Flask, render_template, url_for
from flask_migrate import Migrate

from config import SECRET_KEY, DATABASE_URL
from database import db

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



if __name__ == '__main__':
    app.run(debug=True)