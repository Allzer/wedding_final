from flask_login import UserMixin
from src.Guests.model import Guests
from database import db

class User(UserMixin):
    def __init__(self, guest):
        self.name = guest.first_name
        self.last_name = guest.last_name
        self.id = guest.id
        self.p_number = guest.p_number
        self.password = guest.password
        self.active = True

    @property
    def is_active(self):
        return self.active

def load_user(user_id):
    guest = db.session.get(Guests, int(user_id))
    if guest:
        return User(guest)
    return None
