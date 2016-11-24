I am using this template to build my application. This provides a decent setup to build flask applications.(THis isn't currently doing what I intend to , but I will transform this after I am able to manage a social login integration)

So as to run the app you need to first set the following environment variables:
```shell
export APP_SETTINGS='config.DevelopmentConfig'
```
and Database URL:
```shell
export DATABASE_URL='sqlite:///posts.db'
```
As for Social Login, I intend to use the Flask-Social Library to facilitate social login to the app.[This](https://github.com/mattupstate/flask-social) link has the documentation and sample code for Flask Social Library.

#For postgres Setup use:
First install postgres using :
```shell
sudo apt-get install postgresql postgresql-contrib
```
then use the following command to create a user called postgres
```shell
sudo -u postgres psql postgres
```
and then in the postgres prompt :
use (\password  *password*) cmd to set password

Create database from cli using :
```shell
sudo -u postgres createdb mydb
```
This creates postgres://postgres:*password*@localhost/mydb
thus reset the env variable 
```shell
export DATABASE_URL='postgres://postgres:*password*@localhost/mydb' 
```

#For Migrations:
Create a file called manage.py
add :
```python
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
```


then you can execute:
python manage.py db init
python manage.py db upgrade

#Setting Up Bcrypt
```shell
pip install flask-bcrypt
```
in app.py add:
```python

import flask.ext.bcrypt as Bcrypt

bcrypt = Bcrypt(app)
```

and convert the simple text password to a hash using the bcrypt.generate_password_hash()



# Flask

[Flask](http://flask.pocoo.org/) is a micro web framework powered by Python. It's API is fairly small, making it easy to learn and simple to use. But don't let this fool you, as it's powerful enough to support enterprise-level applications handling large amounts of traffic. You can start small with an app contained entirely in one file, then slowly scale up to multiple files and folders in a well-structured manner as your site becomes more and more complex.


