from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database import db

class Guests(db.Model):

    __tablename__ = 'guest'

    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    patronymic = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String, nullable=False)
    s_n = db.Column(db.String(70), nullable=True)
    p_number = db.Column(db.String, nullable=True)
