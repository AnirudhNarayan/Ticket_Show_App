from .database import db

class User(db.Model):
    __tablename__ = 'User'
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False, unique = True)
    name = db.Column(db.String, nullable= False)
    email_id = db.Column(db.String, nullable= False, unique = True)
    password = db.Column(db.String, nullable= False) 
    blogs = db.relationship('Blog' , backref = 'User')

class Blog(db.Model):
    __tablename__ = 'Blog'
    blog_id = db.Column(db.Integer, unique=True , nullable=False, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    image_url = db.Column(db.String)
    time_stamp = db.Column(db.String, nullable = False)
    poster_id = db.Column(db.Integer, db.ForeignKey('User.user_id'), nullable = False)
