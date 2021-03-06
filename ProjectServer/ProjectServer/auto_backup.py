import os
import time
import sched
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
# 第一个参数确定任务的时间，返回从某个特定的时间到现在经历的秒数
# 第二个参数以某种人为的方式衡量时间
schedule = sched.scheduler(time.time, time.sleep);
def backupsDB():
        # 如果是linux改下路径就可以了

  cmdString = 'D:/php/phpStudy/MySQL/bin/mysqldump -u root --password=root --database abcDataBase > c:/abc_backup.sql';
  os.system(cmdString);
def sendMail():
  _user = "mall@xxxx.com"#发送者的邮箱
  _pwd = "xxxx"#发送者的密码
  _to = "xxxxx@qq.com"#接收者的邮箱
  # 如名字所示Multipart就是分多个部分
  msg = MIMEMultipart()
  msg["Subject"] = "insurance backup"
  msg["From"] = _user
  msg["To"] = _to
  # ---这是文字部分---
  part = MIMEText("insurance backup")
  msg.attach(part)
  # ---这是附件部分---
  # 类型附件
  part = MIMEApplication(open('c:/abc_backup.sql', 'rb').read())
  part.add_header('Content-Disposition', 'attachment', filename="abc_backup.sql")
  msg.attach(part)
  s = smtplib.SMTP("smtp.exmail.qq.com", timeout=30) # 连接smtp邮件服务器,端口默认是25
  s.login(_user, _pwd) # 登陆服务器
  s.sendmail(_user, _to, msg.as_string()) # 发送邮件
  s.close();
def perform_command(cmd, inc):
  # 安排inc秒后再次运行自己，即周期运行
  schedule.enter(inc, 0, perform_command, (cmd, inc));
  os.system(cmd);
  backupsDB();
  sendMail();
def timming_exe(cmd, inc=60):
  # enter用来安排某事件的发生时间，从现在起第n秒开始启动
  schedule.enter(inc, 0, perform_command, (cmd, inc))
  # 持续运行，直到计划时间队列变成空为止
  schedule.run()
if __name__ == '__main__':
  print("show time after 10 seconds:");
  timming_exe("echo %time%", 56400);#Send backups every 56,400 seconds
  #46400 == half day