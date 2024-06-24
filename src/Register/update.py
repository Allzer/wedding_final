from werkzeug.security import generate_password_hash

from src.guests.model import Guests, Admin
from database import db

admins = ["+7(961)645-88-10"]

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

    if form['p_number'] in admins:
        admin = Admin(
            last_name=form["last_name"],
            first_name=form["first_name"],
            p_number=form['p_number'],
            is_admin=True
        )
        db.session.add(admin)
        print("Админ добавлен:", form['p_number'])
    else:
        print("Не админ:", form['p_number'])
    
    db.session.commit()
    print("Изменения внесены")
