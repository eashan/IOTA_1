
##########################
#########Imports##########
##########################
from project import app,db
from project.models import BlogPost
from flask import render_template, redirect, \
    url_for, request, session, flash, g,Blueprint
from functools import wraps
import sqlite3


# ... other required imports ...
from flask.ext.social import Social
from flask.ext.social.datastore import SQLAlchemyConnectionDatastore


home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)
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
#### routes ####
################

# use decorators to link the function to a url
@home_blueprint.route('/')
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


@home_blueprint.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template


