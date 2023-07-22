from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from flask import session
from flask import make_response
import jwt
from datetime import datetime, timedelta
engine = create_engine('sqlite:///database.sqlite3')
Session = scoped_session(sessionmaker(bind=db.engine))
from flask import request, jsonify, current_app
from functools import wraps
import os
from werkzeug.utils import secure_filename
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import send_from_directory
import jwt
from flask import jsonify
from flask import request, g, jsonify
from tasks import send_daily_reminder
from time import perf_counter_ns
from flask import render_template, make_response
from flask_mail import Message
from flask_mail import Mail
from models import Theatre, Shows
from flask import render_template, make_response
mail = Mail(app)






@app.route("/uploads/<path:name>")
def download_file(name):
    return send_from_directory(
        app.config['UPLOAD_FOLDER'], name
    )

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    emailid = data.get('emailid')
    password = data.get('password')
    user = User(emailid=emailid, password=password)
    db.session.add(user)
    db.session.commit()
    message = {'message': 'User created successfully!'}
    return jsonify(message)

import base64

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if not data or 'emailid' not in data or 'password' not in data:
        return jsonify({'message': 'Invalid request'}), 400
    user = User.query.filter_by(emailid=data['emailid'], password=data['password']).first()
    if not user:
        return jsonify({'message': 'Invalid email or password'}), 401
    user_id = user.id
    token = base64.b64encode(str(user_id).encode('utf-8')).decode('utf-8')
    user_object = {
        'user_id': user_id,
        'emailid': user.emailid,
        'password': user.password,
        'token': token
    }
    return jsonify(user_object), 200




from base64 import b64decode

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if len(auth_header.split()) > 1:
                token = auth_header.split()[1]
        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            user_id = int(b64decode(token).decode('utf-8'))
            current_user = User.query.get(user_id)
        except:
            return jsonify({'message': 'Token is invalid'}), 401

        return f(current_user, *args, **kwargs)

    return decorated




@app.route('/get_user', methods=['GET'])
def get_user(current_user):
    user_object = {
       
        'name': current_user.name,
        
    }
    return jsonify(user_object), 200

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'UPLOAD_FOLDER')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/admin_login', methods=['POST'])
def admin_login():
    username = request.json['username']
    admin = Admin.query.filter_by(name=username).first()
    if admin:
        token = jwt.encode({'username': username, 'admin_id': admin.id}, 'secret_key', algorithm='HS256')
        return jsonify({'message': 'Admin login successful', 'token': token, 'admin_id': admin.id})
    else:
        new_admin = Admin(name=username, password='anirudh123')  # Set the default password
        db.session.add(new_admin)
        db.session.commit()
        token = jwt.encode({'username': username, 'admin_id': new_admin.id}, 'secret_key', algorithm='HS256')
        return jsonify({'message': 'New admin added to the database', 'token': token, 'admin_id': new_admin.id})

import jwt
from functools import wraps

def admin_token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Missing token'}), 401

        try:
            decoded_token = jwt.decode(token, 'secret_key', algorithms=['HS256'])
            admin_id = decoded_token.get('admin_id')

            if admin_id:
                g.admin_id = admin_id
                return f(*args, **kwargs)
            else:
                return jsonify({'error': 'Invalid token'}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Expired token'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 401

    return decorated_function

@app.route('/add_theatre', methods=['POST'])
@admin_token_required
def add_theatre():
    venue_name = request.json['venueName']
    place = request.json['place']
    location = request.json['location']
    capacity = request.json['capacity']
    
    admin_id = g.admin_id  
    
    admin = Admin.query.get(admin_id)
    if admin:
        theatre = Theatre(venue_name=venue_name, place=place, location=location, capacity=capacity, admin=admin)
        db.session.add(theatre)
        db.session.commit()
        return jsonify({'message': 'Theatre added successfully'})
    else:
        return jsonify({'error': 'Invalid admin_id'}), 401


@app.route('/get_theatres', methods=['GET'])
@admin_token_required
def get_theatres():
    admin_id = g.admin_id
    admin = Admin.query.get(admin_id)
    if admin:
        theatres = Theatre.query.filter_by(admin=admin).all()
        theatre_list = []
        for theatre in theatres:
            theatre_data = {
                'id': theatre.id,
                'venueName': theatre.venue_name,
                'place': theatre.place,
                'location': theatre.location,
                'capacity': theatre.capacity,
            }
            theatre_list.append(theatre_data)
        return jsonify(theatre_list)
    else:
        return jsonify({'error': 'Invalid admin_id'}), 401

@app.route('/add_show/<int:theatre_id>', methods=['POST'])
@admin_token_required
def add_show(theatre_id):
    show_name = request.json['show_name']
    ratings = request.json['ratings']
    timings = request.json['timings']
    price = request.json['price']
    tags = request.json['tags']

    theatre = Theatre.query.get(theatre_id)
    if theatre:
        show = Shows(show_name=show_name, ratings=ratings, timings=timings, price=price, tags=tags, theatre_id=theatre_id)
        db.session.add(show)
        db.session.commit()
        return jsonify({'message': 'Show added successfully'})
    else:
        return jsonify({'error': 'Invalid theatre_id'}), 401


@app.route('/get_shows/<int:theatreid>', methods=['GET'])
@admin_token_required
def get_shows(theatreid):
    shows = Shows.query.filter_by(theatre_id=theatreid).all()
    if shows:
        shows_data = []
        for show in shows:
            show_data = {
                'id': show.id,
                'show_name': show.show_name,
                'ratings': show.ratings,
                'timings': show.timings,
                'price': show.price,
                'tags': show.tags
            }
            shows_data.append(show_data)

        return jsonify(shows_data)
    else:
        return jsonify([])  


@app.route('/delete_theatre/<int:theatre_id>', methods=['DELETE'])
@cache.cached(timeout=50)
@admin_token_required
def delete_theatre(theatre_id):
    
    theatre = Theatre.query.get(theatre_id)
    if not theatre:
        return jsonify({'error': 'Theatre not found'}), 404
    try:
        
        db.session.delete(theatre)
        db.session.commit()
        return jsonify({'message': 'Theatre deleted successfully'}), 200
    except Exception as e:
        
        return jsonify({'error': 'Failed to delete theatre', 'details': str(e)}), 500

@app.route('/edit_theatre/<int:venueId>', methods=['PUT'])
@admin_token_required
def edit_theatre(venueId):
    
    data = request.get_json()
    
    theatre = Theatre.query.get(venueId)
    if not theatre:
        return jsonify(message='Theatre not found'), 404
    
    theatre.venue_name = data.get('venueName', theatre.venue_name)
    theatre.place = data.get('place', theatre.place)
    theatre.location = data.get('location', theatre.location)
    theatre.capacity = data.get('capacity', theatre.capacity)
    try:
        
        db.session.commit()
        return jsonify(message='Theatre updated successfully'), 200
    except Exception as e:
        
        db.session.rollback()
        return jsonify(message=str(e)), 500

from flask import request, jsonify

@app.route('/delete_show/<int:show_id>', methods=['DELETE'])
@admin_token_required
def delete_show(show_id):
    show = Shows.query.get(show_id)
    if not show:
        return jsonify({'message': 'Show not found'}), 404
    db.session.delete(show)
    db.session.commit()
    return jsonify({'message': 'Show deleted successfully'}), 200


@app.route('/edit_show/<int:show_id>', methods=['PUT'])
@admin_token_required
def edit_show(show_id):
    show = Shows.query.get(show_id)
    if not show:
        return jsonify({'error': 'Show not found'}), 404
    data = request.json
    show.show_name = data.get('show_name', show.show_name)
    show.ratings = data.get('ratings', show.ratings)
    show.timings = data.get('timings', show.timings)
    show.price = data.get('price', show.price)
    show.tags = data.get('tags', show.tags)
    db.session.commit()
    return jsonify({'message': 'Show updated successfully'})



@app.route('/get_display', methods=['GET'])
@cache.cached(timeout=50)
def get_display():
    try:
        theaters = Theatre.query.all()
        theater_list = []
        for theater in theaters:
            shows = Shows.query.filter_by(theatre_id=theater.id).all()
            show_list = []
            for show in shows:
                show_data = {
                    'id': show.id,
                    'show_name': show.show_name,
                    'ratings': show.ratings,
                    'timings': show.timings,
                    'price': show.price,
                    'tags': show.tags
                }
                show_list.append(show_data)
            theater_data = {
                'id': theater.id,
                'venue_name': theater.venue_name,
                'place': theater.place,
                'location': theater.location,
                'capacity': theater.capacity,
                'shows': show_list
            }
            theater_list.append(theater_data)
        return jsonify(theater_list), 200
    except Exception as e:
        return jsonify({'message': 'Error occurred while fetching data'}), 500


@app.route('/shows/<int:show_id>', methods=['GET'])
@cache.cached(timeout=50)
def get_show(show_id):
    try:
        show = Shows.query.get(show_id)
        if show is None:
            return jsonify({'message': 'Show not found'}), 404

        show_data = {
            'id': show.id,
            'show_name': show.show_name,
            'ratings': show.ratings,
            'timings': show.timings,
            'price': show.price,
            'tags': show.tags
        }
        return jsonify(show_data), 200

    except Exception as e:
        return jsonify({'message': 'Error occurred while fetching show data'}), 500

@app.route('/get_show/<int:theater_id>/<int:show_id>', methods=['GET'])
def retrieve_shows(theater_id, show_id):
    try:
        show = Shows.query.filter_by(theatre_id=theater_id, id=show_id).first()
        if show is None:
            return jsonify({'message': 'Show not found'}), 404

        theater = Theatre.query.get(theater_id)
        if theater is None:
            return jsonify({'message': 'Theater not found'}), 404

        show_data = {
            'id': show.id,
            'show_name': show.show_name,
            'ratings': show.ratings,
            'timings': show.timings,
            'price': show.price,
            'tags': show.tags,
            'available_seats': theater.capacity
        }
        return jsonify(show_data), 200

    except Exception as e:
        return jsonify({'message': 'Error occurred while fetching show data'}), 500

@app.route('/update_seats/<int:theater_id>/<int:show_id>', methods=['PUT'])
def update_seats(theater_id, show_id):
    data = request.get_json()
    if 'availableSeats' in data:
        available_seats = data['availableSeats']
        theatre = Theatre.query.get(theater_id)
        if theatre:
            theatre.capacity = available_seats
            db.session.commit()
            return {'message': 'Seats updated successfully'}
        else:
            return {'error': 'Theatre not found'}, 404
    else:
        return {'error': 'Invalid request'}, 400

result = send_daily_reminder.apply_async()
print("The status of daily reminder is:", result.status)


@app.route('/send_monthly_report')
def send_monthly_report():
    theatres = Theatre.query.all()
    report_html = render_template('monthly_report.html', theatres=theatres)
    msg = Message(subject='Monthly Engagement Report',
                  sender=('Sender Name', 'anid6910@gmail.com'),
                  recipients=['21f1001877@ds.study.iitm.ac.in'])
    msg.html = report_html

   
    mail.send(msg)
    
    return 'Monthly report sent successfully'


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True,port=7000)
