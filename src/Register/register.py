from flask import Blueprint, render_template, request
from sqlalchemy import desc

from src.Guests.model import Guests
from src.Register.update import update

reg = Blueprint('reg', __name__, template_folder='templates', static_folder='static')

@reg.route('/')
def index():
    # if request.method == 'POST':
    #     form = request.form
    #     update(form)
    #     all_tasks = Guests.query.order_by(desc(Guests.id)).all()

    # elif request.method == 'GET':
    #     all_tasks = Guests.query.order_by(desc(Guests.id)).all()

    # return render_template(
    #     'tasks.html',
    #     title='Tasks',
    #     tasks=all_tasks
    # )
    return render_template('reg.html', title="Регистрация")
 





