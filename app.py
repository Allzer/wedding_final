from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from config import SECRET_KEY, DATABASE_URL
from database import db
from src.Register.register import reg
from src.routes.auth import auth
from src.routes.main import main
from src.profile.profile import profile
from src.user import load_user

app = Flask(__name__)
app.secret_key = SECRET_KEY

app.register_blueprint(reg, url_prefix='/registrations')
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(main)
app.register_blueprint(profile, url_prefix='/profile')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
login_manager.user_loader(load_user)


if __name__ == '__main__':
    app.run(debug=True)
