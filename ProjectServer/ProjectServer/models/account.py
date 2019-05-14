from flask_login import UserMixin, login_manager
from werkzeug.security import generate_password_hash, check_password_hash

from exts import db


class AcountUser(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_email = db.Column(db.String(24), nullable=False)
    user_name = db.Column(db.String(24), nullable=False)
    user_password = db.Column(db.String(100), default='123456')
    user_phone = db.Column(db.String(12), nullable=False)
    user_firstName=db.Column(db.String(24), nullable=False)
    user_lastName = db.Column(db.String(24), nullable=False)
    user_country = db.Column(db.String(24))
    user_photo = db.Column(db.LargeBinary(length=(2 ** 32) - 1))
    validity = db.Column(db.DATETIME, nullable=False)


class AcountEmployee(db.Model, UserMixin):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    employ_email = db.Column(db.String(24), nullable=False)
    employ_name = db.Column(db.String(24), nullable=False)
    empliye_password = db.Column(db.String(100), default='123456')
    employ_firstName = db.Column(db.String(24), nullable=False)
    employ_lastName = db.Column(db.String(24), nullable=False)
    employ_country = db.Column(db.String(24), nullable=False)
    employ_phone = db.Column(db.String(24), nullable=False)
    employ_photo = db.Column(db.LargeBinary(length=(2 ** 32) - 1))

