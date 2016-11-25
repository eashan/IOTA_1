from flask_wtf import Form 
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(Form):
	username = TextField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	
class SignupForm(Form):
	username = TextField('Username', validators=[DataRequired()])
	description = TextField('Description', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
