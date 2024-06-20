from flask import Blueprint, render_template, request
from flask_login import login_required

main = Blueprint('main', __name__)

@main.route("/index")
@main.route("/")
@login_required
def index():
    user_agent = request.user_agent.string
    if 'Mobile' in user_agent or 'Android' in user_agent or 'iPhone' in user_agent:
        return render_template('index.html')
    else:
        return render_template('index_desktop.html')
