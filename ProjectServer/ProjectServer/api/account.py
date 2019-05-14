import datetime

from flask import request, jsonify, Blueprint, json, render_template, current_app, app
from flask_cors import cross_origin

from exts import db
from models.account import AcountUser, AcountEmployee

api_account = Blueprint('account', __name__)

@api_account.route('/register', methods=['POST'])
@cross_origin()#通过装饰路线具体CORS

def creat_account():
    result = jsonify({"status_code": 100100})
    data = request.get_data()
    jsonList = json.loads(data)
    getName = jsonList['name']
    getPassword = jsonList['password']
    getEmail= jsonList['email']
    getPhone = jsonList['phone']
    check_name = AcountUser.query.filter(AcountUser.user_name == getName).first()
    if check_name:
            result = jsonify({"status_code": 100110})
            return result
    else:
            acountuser = AcountUser(user_name=getName,
                                    user_password=getPassword,
                                    user_email=getEmail,
                                    user_phone=getPhone)
            db.session.add(acountuser)
            db.session.commit()
            result = jsonify({"status_code": 100111})
            return result
    return result

@api_account.route('/login',methods=['POST','GET'])
@cross_origin()#通过装饰路线具体CORS

def login_account():

    result = jsonify({"status_code": 100200})  # login fail
    jsonList = json.loads(request.get_data(as_text=True))
    accounttype = jsonList['type']
    print(accounttype)
    if accounttype == 'customer':
        getName = jsonList['name']
        getPassword = jsonList['password']
        check_account = AcountUser.query.filter(AcountUser.user_name == getName).first()
        if check_account:
            check_passord = AcountUser.query.filter(AcountUser.user_name == getName, AcountUser.user_password == getPassword ).first()
            if check_passord:
                result = jsonify({'status_code': 100211})
                print(result)
            else:
                result = jsonify({'status_code': 100220})
        else:
            result = jsonify({"status_code": 100210})

    if accounttype == "employee":
        EmployeeName = jsonList['name']
        EmploeePassword = jsonList['password']
        check_account = AcountEmployee.query.filter( AcountEmployee.employ_name == EmployeeName).first()
        if check_account:
            check_passord = AcountUser.query.filter( AcountEmployee.employ_name == EmployeeName,
                                                     AcountEmployee.empliye_password == EmploeePassword).first()
            if check_passord:
                result = jsonify({'status_code': 100211})
            else:
                result = jsonify({'status_code': 1002202})
        else:
            result = jsonify({"status_code": 1002102})
    print("result:")
    a = str(result)
    print(a)
    print("finished")
    # print(result["status_code"])
    return result

@api_account.route('/server_test')
@cross_origin()#通过装饰路线具体CORS

def server_test():

    return "success"


@api_account.route('/get_someone_details',methods=['POST','GET'])
@cross_origin()#通过装饰路线具体CORS
def get_someone_details():
    data = request.get_data()
    jsonList = json.loads(data)
    userName = jsonList['name']
    print(userName)
    user = AcountUser.query.filter(AcountUser.user_name == userName).first()
    userdetails = {
        "email": user.user_email,
        "phone":user.user_phone
    }

    return jsonify(userdetails)


@api_account.route('/get_account_details',methods=['POST','GET'])
@cross_origin()#通过装饰路线具体CORS
def get_account_details():
    data = request.get_data()
    jsonList = json.loads(data)
    type=jsonList['type']
    if (type =='user'):
        userName = jsonList['name']
        print("useeeeeeeeeeeeeeeeeeeeee")
        print(userName)
        print(userName)
        user = AcountUser.query.filter(AcountUser.user_name == userName).first()
        print(user)
        userdetails = {
            "status_code": "success",
            "email": user.user_email,
            "phone":user.user_phone,
            "firstName": user.user_firstName,
            "lastName": user.user_lastName,
            "id":user.id,
            "userName":user.user_name,
            "password":user.user_password,
            "country":user.user_country,
            "photo":str(user.user_photo)[2:-1]

        }
    if(type == "employee"):
        Name = jsonList['name']
        print(str(Name))
        account = AcountEmployee.query.filter(AcountEmployee.employ_name == Name).first()
        print(str(account))
        userdetails = {
            "status_code": "success",
            "id":account.id,
            "email":account.employ_email,
            "name":account.employ_name,
            "password": account.empliye_password,
            "firstName":account.employ_firstName,
            "lastName":account.employ_lastName,
            "country":account.employ_country,
            "phone":account.employ_phone,
            "photo": str(account.employ_photo)[2:-1]
        }
        print(str(account.employ_photo)[2:-1])
        # employ_firstName = db.Column(db.String(24), nullable=False)
        # employ_lastName = db.Column(db.String(24), nullable=False)
        # employ_country = db.Column(db.String(24), nullable=False)
        # employ_phone = db.Column(db.String(24), nullable=False)
    return jsonify(userdetails)
# class AcountUser(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     user_email = db.Column(db.String(24), nullable=False)
#     user_name = db.Column(db.String(24), nullable=False)
#     user_password = db.Column(db.String(100), nullable=False)
#     user_phone = db.Column(db.String(12), nullable=False)
#     user_firstName=db.Column(db.String(24), nullable=False)
#     user_lastName = db.Column(db.String(24), nullable=False)
#
# class AcountEmployee(db.Model):
#     __tablename__ = 'employees'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     employ_email = db.Column(db.String(24), nullable=False)
#     employ_name = db.Column(db.String(24), nullable=False)
#     empliye_password = db.Column(db.String(100), nullable=False)

@api_account.route('/update_account_details',methods=['POST','GET'])
@cross_origin()#通过装饰路线具体CORS
def update_account_details():
    data = request.get_data()
    jsonList = json.loads(data)
    type=jsonList['type']
    print("update det")
    if (type =='user'):
        print("user:")

        userName = jsonList["name"]
        user = AcountUser.query.filter(AcountUser.user_name == userName).first()
        if (user):
            print("there is someone called ")
        print(userName)
        print(jsonList['email'])
        email = jsonList['email']
        phone = jsonList['phone']
        firstName = jsonList['firstName']
        lsatName = jsonList['lastName']
        password = jsonList['password']
        country = jsonList['country']
        print(country)
        user.user_email=email
        
        user.user_phone = phone
        user.user_firstName=firstName
        user.user_lastName=lsatName
        user.user_password=password
        user.user_country = country

        db.session.add(user)
        db.session.commit()
        user = AcountUser.query.filter(AcountUser.user_name == userName).first()
        print(user.user_country)
    if(type == "employee"):
        print("em: ")
        name = jsonList['name']
        print(name)
        account = AcountEmployee.query.filter(AcountEmployee.employ_name == name).first()
        if(account):
            print("there is someone called")
        print(name)
        email = jsonList['email']
        phone = jsonList['phone']
        firstName = jsonList['firstName']
        lsatName = jsonList['lastName']
        password = jsonList['password']
        country = jsonList['country']
        print(country)
        account.employ_email=email
        account.employ_phone=phone
        account.employ_firstName =firstName
        account.employ_lastName = lsatName
        account.empliye_password = password
        account.employ_country = country
        db.session.add(account)
        db.session.commit()
    return jsonify({"status":"success"})

@api_account.route('/get_validity',methods=['POST','GET'])
@cross_origin()#通过装饰路线具体CORS
def get_validity():
    data = request.get_data()
    jsonList = json.loads(data)
    userName = jsonList["username"]
    user = AcountUser.query.filter(AcountUser.user_name == userName).first()

    return jsonify({"validity": user.validity})

@api_account.route('/update_validity',methods=['POST','GET'])
@cross_origin()#通过装饰路线具体CORS
def update_validity():
    data = request.get_data()
    jsonList = json.loads(data)
    userName = jsonList["username"]
    user = AcountUser.query.filter(AcountUser.user_name == userName).first()
    delta = datetime.timedelta(days=30)
    newvalidity = user.validity + delta
    user.validity = newvalidity
    db.session.add(user)
    db.session.commit()
    #f
    return jsonify({"status":"success"})