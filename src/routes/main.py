from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from database import db

from src.guests.model import Accept

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

@main.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == "POST":
        form = request.form
        if len(form['menu']) > 0 and len(form['music']) > 0 and len(form['hist']) > 0 and len(form['fact']) > 0 \
        and len(form['question']) > 0:
            a = Accept(
            guest_id=current_user.id,
            menu=form['menu'],
            music=form['music'],
            hist=form['hist'],
            fact=form['fact'],
            surprise=form['surprise'],
            question=form['question'],
            )

            db.session.add(a)
            db.session.commit()
            print("Изменения внесены")

            return redirect(url_for('main.index'))

    return render_template('form.html')
