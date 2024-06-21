from werkzeug.security import generate_password_hash

from src.guests.model import Guests
from database import db


def update(form):
    g = Guests(
        last_name=form["last_name"],
        first_name=form["first_name"],
        patronymic=form["patronymic"],
        password=generate_password_hash(form['psw']),
        s_n=form['s_n'],
        p_number=form['p_number'],
    )

    db.session.add(g)
    db.session.commit()
    print("Изменения внесены")
