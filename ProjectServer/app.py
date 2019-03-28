from flask import Flask
import config
from api.account import *

from exts import db

app = Flask(__name__)
app.register_blueprint(api_account, url_prefix='/account')
app.config.from_object(config)
db.init_app(app)

if __name__ == '__main__':
    app.run()


