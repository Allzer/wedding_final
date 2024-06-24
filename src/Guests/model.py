from database import db

class Guests(db.Model):
    __tablename__ = 'guest'

    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    patronymic = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    s_n = db.Column(db.String(70), nullable=True, unique=True)
    p_number = db.Column(db.String(20), nullable=True, unique=True)

    admin = db.relationship('Admin', backref='guest', uselist=False)
    accept = db.relationship('Accept', backref='guest', uselist=False)


class Admin(db.Model):
    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    p_number = db.Column(db.String(20), db.ForeignKey('guest.p_number'), nullable=False)
    is_admin = db.Column(db.Boolean, default=True)

class Accept(db.Model):
    __tablename__ = 'accept'

    guest_id = db.Column(db.Integer, db.ForeignKey('guest.id'), primary_key=True, nullable=False)
    menu = db.Column(db.String(20), nullable=False)
    music = db.Column(db.String(20), nullable=False)
    hist = db.Column(db.String(20), nullable=False)
    fact = db.Column(db.String(20), nullable=False)
    surprise = db.Column(db.String(20), nullable=False)
    question = db.Column(db.String(20), nullable=False)


    

    

