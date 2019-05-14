from flask import Flask
from flask_admin.contrib.sqla import ModelView
import config
from api.account import *
from api.report import *
from flask_admin import Admin
from exts import db
app = Flask(__name__)
app.register_blueprint(api_account, url_prefix='/account')
app.register_blueprint(api_report,url_prefix='/report')
app.config.from_object(config)
db.init_app(app)
admin = Admin(app, name='管理后台')
admin.add_view(ModelView(AcountUser, db.session))
admin.add_view(ModelView(Reports, db.session))
admin.add_view(ModelView(AcountEmployee, db.session))




limiter = Limiter(
    app,
    key_func= get_remote_address,
    default_limits=["5000 per day","200 per hour"]
)
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)


