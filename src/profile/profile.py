from flask import Blueprint, render_template
from flask_login import login_required, current_user

from src.guests.model import Guests

profile = Blueprint('profile', __name__, template_folder='templates', static_folder='static')

@profile.route('/')
@login_required
def prof():
    if not current_user.admin:
        return "Доступ запрещен", 403

    guests = Guests.query.all()
    return render_template('profile.html', title='Профиль', guests=guests)
