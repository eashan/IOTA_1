from app import db
from models import BlogPost

#create the database and the db tables
db.create_all()


#insert
db.session.add(BlogPost("Good WIll Hunting","Awesome movie"))
db.session.add(BlogPost("Die hard","Awesome movie"))
db.session.add(BlogPost("Breakfast Club","Awesome movie"))




#commit the changes
db.session.commit()