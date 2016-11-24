# import the Flask class from the flask module
from flask import Flask
    
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
import os

# ... other required imports ...
from flask.ext.social import Social
from flask.ext.social.datastore import SQLAlchemyConnectionDatastore



################
#### config ####
################
app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config.from_object(os.environ['APP_SETTINGS'])

#create the sqlalchemy object
db = SQLAlchemy(app)


from project.users.views import users_blueprint
from project.home.views import home_blueprint
#register our blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)