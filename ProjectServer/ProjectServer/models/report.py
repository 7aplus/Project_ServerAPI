from exts import db

class Reports(db.Model):
    __tablename__ = 'reports'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_status = db.Column(db.String(4), nullable=False)
    employee_feedback = db.Column(db.TEXT(length=10000))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey("employees.id"))
    report_describe = db.Column(db.TEXT(length=10000))
    create_time = db.Column(db.TIMESTAMP, nullable=False)
    lost_time = db.Column(db.DATETIME, nullable=False)
    lost_location = db.Column(db.String(100), nullable=False)
    photo=db.Column(db.LargeBinary(length=(2**32)-1))



class Insurance(db.Model):
    __tablename__ = 'insurances'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    create_time = db.Column(db.TIMESTAMP, nullable=False)
    insurance_start = db.Column(db.DATETIME, nullable=False)
    insurance_end = db.Column(db.DATETIME, nullable=False)