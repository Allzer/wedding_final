from flask import Blueprint, render_template
from flask_login import current_user


profile = Blueprint('profile', __name__)

@profile.route('/')
def prof():
    name = current_user.name
    last_name = current_user.last_name
    return render_template('profile.html', title='Профиль', name=name, l_name=last_name)