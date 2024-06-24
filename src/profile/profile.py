from flask import Blueprint, render_template
from flask_login import login_required, current_user

from src.guests.model import Accept, Guests
from sqlalchemy.orm import aliased


from database import db

profile = Blueprint('profile', __name__, template_folder='templates', static_folder='static')

@profile.route('/')
@login_required
def prof():
    if not current_user.admin:
        return "Доступ запрещен", 403

    
    results = db.session.query(Guests, Accept).join(Accept, Guests.id == Accept.guest_id).all()
    all = db.session.query(Guests).all()

    return render_template('profile.html', title='Профиль', guests=results, all=all)
