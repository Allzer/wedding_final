from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database import db

class Guests(db.Model):

    __tablename__ = 'guest'

    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    patronymic = db.Column(db.String(20), nullable=False)
    contact_id = db.Column(db.Integer, ForeignKey('contact.contact_id'), unique=True)

    password = db.Column(db.String, nullable=False)
    check_password = db.Column(db.String, nullable=False)

    contact = relationship("Contacts", uselist=False, back_populates="guest")

class Contacts(db.Model):

    __tablename__ = 'contact'

    contact_id = db.Column(db.Integer, primary_key=True)
    telegram = db.Column(db.String(70), nullable=True)
    vk = db.Column(db.String(70), nullable=True)
    p_number = db.Column(db.Integer, nullable=True)

    guest = relationship("Guests", back_populates="contact")