# import the Flask class from the flask module
from flask import Flask, render_template, redirect, \
    url_for, request, session, flash, g
from flask.ext.sqlalchemy import SQLAlchemy
from functools import wraps
import sqlite3
import os

# ... other required imports ...
from flask.ext.social import Social
from flask.ext.social.datastore import SQLAlchemyConnectionDatastore


##########################
#### helper functions ####
##########################

# login required decorator
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('users.login'))
    return wrap

################
#### config ####
################
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

#create the sqlalchemy object
db = SQLAlchemy(app)

from models import *
from project.users.views import users_blueprint

#register our blueprints
app.register_blueprint(users_blueprint)






################
#### routes ####
################

# use decorators to link the function to a url
@app.route('/')
@login_required
def home():
    posts = []

    try:
        query = BlogPost.query.all()
        for row in query:
            posts.append(dict(author = row.author,title = row.title, description = row.description))

    except sqlite3.OperationalError:
        flash ("You have no db")
    return render_template('index.html', posts=posts)  # render a template


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template




# connect to database
#def connect_db():
#    return sqlite3.connect(app.database)

####################
#### run server ####
####################

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
