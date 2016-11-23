I am using this template to build my application. This provides a decent setup to build flask applications.(THis isn't currently doing what I intend to , but I will transform this after I am able to manage a social login integration)

So as to run the app you need to first set the following environment variables:
export APP_SETTINGS='config.DevelopmentConfig'
and Database URI:
export DATABASE_URL='sqlite:///posts.db'

As for Social Login, I intend to use the Flask-Social Library to facilitate social login to the app.[This](https://github.com/mattupstate/flask-social) link has the documentation and sample code for Flask Social Library.

For postgres Setup use:

sudo -u postgres psql postgres

and then in the postgres prompt :
use (\password  *password*) cmd to set password

Create database from cli using :
 sudo -u postgres createdb mydb

This creates postgres://postgres:*password*@localhost/mydb

For Migrations:
Create a file called manage.py
add :
///
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import os

from app import app, db

app.config.from_object(os.environ['APP_SETTINGS'])
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()

///

then you can execute:
python manage.py db init
python manage.py db upgrade



# Introduction to Flask

[Flask](http://flask.pocoo.org/) is a micro web framework powered by Python. It's API is fairly small, making it easy to learn and simple to use. But don't let this fool you, as it's powerful enough to support enterprise-level applications handling large amounts of traffic. You can start small with an app contained entirely in one file, then slowly scale up to multiple files and folders in a well-structured manner as your site becomes more and more complex.

![real_python_logo](https://raw.githubusercontent.com/realpython/about/master/rp_small.png)

## Contents


| Part |      Title                |  Blog URL | Video URL |
|------|---------------------------|-----------| ----------|
| 1    |  Setting Up a Static Site | [Link](http://www.realpython.com/blog/python/introduction-to-flask-part-1-setting-up-a-static-site)      | [Link](https://www.youtube.com/watch?v=Gix_zeTrT7E) |
| 2    |  Creating a login page | [Link](http://www.realpython.com/blog/python/introduction-to-flask-part-2-creating-a-login-page)      | [Link](https://www.youtube.com/watch?v=IrlqSQNwoDA) |
| 3    |  User Authentication  | N/A      | [Link](https://www.youtube.com/watch?v=xUL2WeGX830) |
| 4    |  Template Inheritance | N/A      | [Link](https://www.youtube.com/watch?v=343KEx1K5KQ) |
| 5    |  Databases | N/A      | [Link](https://www.youtube.com/watch?v=tpOaFQcfmhw) |
| 6    |  List Comprehensions | N/A      | [Link](https://www.youtube.com/watch?v=Ft3HS37hWpc) |
| 7    |  Unit Tests | N/A      | [Link](https://www.youtube.com/watch?v=TUnOHGolpvo) |


