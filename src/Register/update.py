from Guests.model import Guests
from database import db


def update(form):
    t = Guests(
        title=form["title"],
        description=form["description"],
        date=form["date"],
        importance=form["importance"]
    )

    db.session.add(t)
    db.session.commit()
    print("Изменения внесены")


