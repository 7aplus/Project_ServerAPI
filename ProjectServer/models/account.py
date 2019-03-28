from exts import db


class AcountUser(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_email = db.Column(db.String(24), nullable=False)
    user_name = db.Column(db.String(24), nullable=False)
    user_password = db.Column(db.String(100), nullable=False)
    user_phone = db.Column(db.String(12), nullable=False)


class AcountEmployee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    employ_email = db.Column(db.String(24), nullable=False)
    employ_name = db.Column(db.String(24), nullable=False)
    empliye_password = db.Column(db.String(100), nullable=False)