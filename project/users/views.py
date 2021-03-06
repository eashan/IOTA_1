
#################
#### imports ####
#################
from flask import flash, redirect, render_template, request, \
session, url_for, Blueprint
from project.models import NGO,bcrypt
from functools import wraps
from form import LoginForm, SignupForm
from project import db
################
#### config ####
################

users_blueprint = Blueprint(
	'users', __name__,
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



# route for handling the login page logic
@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    form = LoginForm(request.form)

    if request.method == 'POST':
    	if form.validate_on_submit():
    		user = NGO.query.filter_by(name=request.form['username']).first()
    		if(user is not None and bcrypt.check_password_hash(user.password,request.form['password'].encode('utf-8'))):
	            session['logged_in'] = True
	            flash('You were logged in.')
	            return redirect(url_for('home.home'))
        	else:
	        	error = 'Invalid Credentials. Please try again.'


    return render_template('login.html',form=form ,error=error)

@users_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
	error = None
	
	form = SignupForm(request.form)
	
	if request.method == 'POST':
	    	if form.validate_on_submit():
		    	user = NGO.query.filter_by(name=request.form['username']).first()
		    	if(user is not None):
			    		error = 'Already Registered'
		        else:
			            session['logged_in'] = True
			            db.session.add(NGO(request.form['username'],request.form['description'],request.form['password']))
			            db.session.commit()
			            flash('You were logged in.')
			            return redirect(url_for('home.home'))
   	return render_template('signup.html',form=form ,error=error)

@users_blueprint.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('home.welcome'))
