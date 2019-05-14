import base64
import os
import time

from flask import request, jsonify, Blueprint, json, render_template, current_app, app
from flask_cors import cross_origin
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.utils import secure_filename


from exts import db
from models.report import Reports
from models.account import *

# id = db.Column(db.Integer, primary_key=True, autoincrement=True)
# order_id = db.Column(db.Integer, nullable=False)
# user_firstName = db.Column(db.String(24), nullable=False)
# user_secondName = db.Column(db.String(24), nullable=False)
# user_status = db.Column(db.Integer, nullable=False)
# employee_feedback = db.Column(db.TEXT(length=10000))
# user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
# employee_id = db.Column(db.Integer, db.ForeignKey("employees.id"))
# report_describe = db.Column(db.TEXT(length=10000))
# create_time = db.Column(db.TIMESTAMP, nullable=False)
api_report = Blueprint('report', __name__)
UPLOAD_FOLDER = 'upload'




@api_report.route('/get_all_report', methods=['POST'])
@cross_origin()#通过装饰路线具体CORS

def get_all_report():
    data = request.get_data()
    jsonList = json.loads(data)
    getManger = jsonList['type']
    result = jsonify({"status_code": 100100})
    allreports = Reports.query.all()
    myresult={}
    myresult["status_code"] = "success"
    print(myresult)
    reports = []
    for instance in allreports:
        user = AcountUser.query.filter(AcountUser.id == instance.user_id).first()
        eac={
            "firstName":user.user_firstName,
            "lastName": user.user_lastName,
            "status": instance.user_status,
            "order":  instance.id,
            "userName": user.user_name
        }
        reports.append(eac)
    myresult["reports"]=reports
    return jsonify(myresult)


@api_report.route('/get_report_bystatus', methods=['POST'])
@cross_origin()#通过装饰路线具体CORS

def get_report_status():
    data = request.get_data()
    jsonList = json.loads(data)
    report_type = jsonList['type']
    check=0
    if report_type =="accept":
        check = 1
    elif report_type =="reject":
        check = -1
    elif report_type =="waitting":
        check=0
    result = jsonify({"status_code": 100100})
    allreports = Reports.query.all()
    myresult={}
    myresult["status_code"] = "success"
    print(myresult)
    reports = []
    for instance in allreports:
        user = AcountUser.query.filter(AcountUser.id == instance.user_id).first()
        eac={
            "firstName":user.user_firstName,
            "lastName": user.user_lastName,
            "status": instance.user_status,
            "order":  instance.id,
            "userName": user.user_name
        }
        if instance.user_status == check:
            reports.append(eac)
    myresult["reports"]=reports
    return jsonify(myresult)


@api_report.route('/get_report',methods=['post'])
@cross_origin()#通过装饰路线具体CORS
def get_report():
    data = request.get_data()
    jsonList = json.loads(data)
    reportid = jsonList['query']
    getReport = Reports.query.filter(Reports.id == reportid).first()
    orderid = reportid
    username = (AcountUser.query.filter(AcountUser.id == getReport.user_id).first()).user_name
    firstname = (AcountUser.query.filter(AcountUser.id == getReport.user_id).first()).user_firstName
    lastname = (AcountUser.query.filter(AcountUser.id == getReport.user_id).first()).user_lastName

    time = getReport.create_time
    description = getReport.report_describe
    feedback =getReport.employee_feedback
    location = getReport.lost_location
    photo = str(getReport.photo)[2:-1]
    result = {
        "status_code":"success",
        "orderid":orderid,
        "username" :username,
        "firstname":firstname,
        "lastname":lastname,
        "time":time,
        "description":description,
        "feedback":feedback,
        "location":location,
        "photo": photo

    }
    return jsonify(result)



@api_report.route('/create_report', methods=['POST'])
@cross_origin()#通过装饰路线具体CORS
def create_report():
    data = request.get_data()
    jsonList = json.loads(data)
    username=jsonList['username']
    print("username:  "+str(username))
    location= jsonList['location']
    print("location: "+str(location))
    lost_time = jsonList['time']
    print("lost_time: "+str(time))
    allreports = Reports.query.all()
    create_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    description = jsonList['message']
    print("message: "+str(description))
    photo_base64 = jsonList['photo']
    photo_base64 = bytearray(photo_base64, encoding="utf-8")
    print("THE TYPE OF PHOTO_BASE64")
    print(type(photo_base64))
    status = 0
    user = AcountUser.query.filter(AcountUser.user_name == username).first()
    user_id = user.id

    # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # order_id = db.Column(db.Integer, nullable=False, autoincrement=True)
    # user_status = db.Column(db.String(4), nullable=False)
    # employee_feedback = db.Column(db.TEXT(length=10000))
    # user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    # employee_id = db.Column(db.Integer, db.ForeignKey("employees.id"))
    # report_describe = db.Column(db.TEXT(length=10000))
    # create_time = db.Column(db.TIMESTAMP, nullable=False)
    # lost_time = db.Column(db.DATETIME, nullable=False)
    # lost_location = db.Column(db.String(10), nullable=False)
    employee_id = len(Reports.query.all())%3 + 1

    report = Reports(
        user_status = status,
        user_id = user_id,
        employee_id = employee_id,
        report_describe = description,
        create_time = create_time,
        lost_time = lost_time,
        lost_location = location,
        employee_feedback="",
        photo=photo_base64
    )
    print("success photo")
    db.session.add(report)
    db.session.commit()

    getReport = Reports.query.filter(Reports.create_time == create_time).first()
    result={
        "status_code": "success",
        "orderId": getReport.id,
        "photo_base64": str(report.photo)[2:-1]
    }
    return jsonify(result)

@api_report.route('/get_someone_report',methods=['post'])
@cross_origin()#通过装饰路线具体CORS
def get_someone_report():
    data = request.get_data()
    jsonList = json.loads(data)
    getuserName = jsonList['username']
    print(getuserName)
    user = AcountUser.query.filter(AcountUser.user_name == getuserName).first()
    userid=user.id
    print(userid)
    result = jsonify({"status_code": 100100})

    allreports = Reports.query.filter_by(user_id = str(userid))
    myresult = {}
    myresult["status_code"] = "success"
    reports = []
    for instance in allreports:
        user = AcountUser.query.filter(AcountUser.id == instance.user_id).first()
        eac = {
            "status": instance.user_status,
            "orderId": instance.id,
            "feedback":instance.employee_feedback,
            "time":instance.create_time,
            "location":instance.lost_location
        }
        reports.append(eac)

    myresult["reports"] = reports
    print(myresult)
    return jsonify(myresult)

@api_report.route('/update_report',methods=['post'])
@cross_origin()#通过装饰路线具体CORS
def update_report():
    data = request.get_data()
    jsonList = json.loads(data)
    reportid = jsonList['orderId']
    print(reportid)
    status = 0;
    if jsonList['operate'] == "accept":
        status = 1
    else:
        status = -1
    getReport = Reports.query.filter(Reports.id == reportid).first()
    print(reportid)
    print(status)
    feedback = ""
    feedback += jsonList['text']

    getReport.user_status=status
    getReport.employee_feedback = feedback
    db.session.add(getReport)
    db.session.commit()

    return jsonify({"status_code":"success"})

@api_report.route('/search_report',methods=['post'])
@cross_origin()#通过装饰路线具体CORS
def search_report():
    data = request.get_data()
    jsonList = json.loads(data)
    reportid=jsonList['search']
    print("search id ")
    print(reportid)
    if(Reports.query.filter(Reports.id == reportid).first()):
        getReport = Reports.query.filter(Reports.id == reportid).first()
        print(getReport)
        getReport = Reports.query.filter(Reports.id == reportid).first()
        orderid = reportid
        username = (AcountUser.query.filter(AcountUser.id == getReport.user_id).first()).user_name
        firstname = (AcountUser.query.filter(AcountUser.id == getReport.user_id).first()).user_firstName
        lastname = (AcountUser.query.filter(AcountUser.id == getReport.user_id).first()).user_lastName
        user_status = getReport.user_status
        time = getReport.create_time
        description = getReport.report_describe
        feedback = getReport.employee_feedback
        location = getReport.lost_location
        photo = str(getReport.photo)[2:-1]
        result = {
            "status_code": "success",
            "order": orderid,
            "status": user_status,
            "userName": username,
            "firstName": firstname,
            "lastName": lastname,
            "time": time,
            "description": description,
            "feedback": feedback,
            "location": location,
            "photo": photo

        }
        return jsonify(result)
    else:
        print("search report None")
        return jsonify({"status_code": "None"})
