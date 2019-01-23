from flask import Flask
from flask_migrate import Migrate

import os
import configparser

application = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

appenv = os.environ.get('APP_ENV')
config = configparser.ConfigParser()
config.read('app/db-config.ini')

if appenv != 'development' and appenv is not None:
    if appenv not in config:
        print("ERROR: You must add DB details for this environment to db-config.ini.")
    else:
        host = config[appenv]['host']
        db = config[appenv]['db']
        username = config[appenv]['username']
        password = config[appenv]['password']
        
        application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+ username +':'+ password +'@'+ host + '/' + db + "?charset=utf8mb4"
else:
    application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'development-db.sqlite')

application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['OUR_EPOCH'] = 1531953129


from .Models import db
db.init_app(application)
migrate = Migrate(application, db)


# Every time we create a new endpoint file in the 'Endpoints' folder, import it here
from .Endpoints import Auth, RequestID, Posts
# then register its Blueprint variable here
application.register_blueprint(Auth.auth)
application.register_blueprint(RequestID.request_id)
application.register_blueprint(Posts.posts)


if __name__ == '__main__':
    application.run(debug=True)
