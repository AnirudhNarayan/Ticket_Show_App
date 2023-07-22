from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token
from werkzeug.security import check_password_hash
from datetime import datetime
from flask_cors import CORS
from flask_caching import Cache

app = Flask(__name__, static_folder='/UPLOAD_FOLDER/',template_folder='templates')
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ticket_show.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'anirudh123'
jwt = JWTManager(app)
db = SQLAlchemy(app)
app.config["CACHE_TYPE"] = "RedisCache"
app.config["CACHE_DEFAULT_TIMEOUT"] = 50 # Update the timeout value to 50 seconds
app.config["CACHE_REDIS_HOST"] = "localhost"
app.config["CACHE_REDIS_PORT"] = 6379
app.config["CACHE_REDIS_DB"] = 9
# Initialize cache
cache = Cache(app)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'anid6910@gmail.com'
app.config['MAIL_PASSWORD'] = 'protozoa2323'




class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    emailid = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

class Admin(db.Model):
   
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)

    # @classmethod
    # def get_admin(cls):
    #     return cls.query.first()

class Theatre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    venue_name = db.Column(db.String(80), nullable=False)
    place = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)
    admin = db.relationship('Admin', backref=db.backref('theatres', lazy=True))

class Shows(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    show_name = db.Column(db.String(80), nullable=False)
    ratings = db.Column(db.Float, nullable=False)
    timings = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    tags = db.Column(db.String(255), nullable=False)
    theatre_id = db.Column(db.Integer, db.ForeignKey('theatre.id'), nullable=False)

  

# Uncomment the below while running original app

# db.create_all()

# admin = Admin.query.filter_by(name='Admin').first()
# if admin is None:
#     admin = Admin(name='Admin', password='anirudh123')
#     db.session.add(admin)
#     db.session.commit()

