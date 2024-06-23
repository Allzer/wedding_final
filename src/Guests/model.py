from database import db

class Guests(db.Model):
    __tablename__ = 'guest'

    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    patronymic = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String, nullable=False)
    s_n = db.Column(db.String(70), nullable=True, unique=True)
    p_number = db.Column(db.String(20), nullable=True, unique=True)

    admin = db.relationship('Admin', backref='guest', uselist=False)


class Admin(db.Model):
    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    p_number = db.Column(db.String(20), db.ForeignKey('guest.p_number'), nullable=False, unique=True)
    is_admin = db.Column(db.Boolean, default=True)