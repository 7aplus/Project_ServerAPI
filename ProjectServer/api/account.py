from flask import request, jsonify, Blueprint, json
from exts import db
from models.account import AcountUser
api_account = Blueprint('account', __name__)

@api_account.route('/register', methods=['POST'])
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

@api_account.route('/login',methods=['POST'])
def login_account():
    result = jsonify({"status_code": 100200})  # login fail
    logindata = request.get_data()
    jsonList = json.loads(logindata)
    accounttype = jsonList['type']
    if accounttype == 'customer':
        getName = jsonList['name']
        getPassword = jsonList['password']
        check_account = AcountUser.query.filter(AcountUser.user_name == getName).first()
        if check_account:
            check_passord = AcountUser.query.filter(AcountUser.user_name == getName, AcountUser.user_password == getPassword ).first()
            if check_passord:
                result = jsonify({'status_code': 100211})
            else:
                result = jsonify({'status_code': 100220})
        else:
            result = jsonify({"status_code": 100210})
        return result

    if accounttype == "employee":
        return 'em'

    return result
