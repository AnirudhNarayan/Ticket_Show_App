from jinja2 import Template
from weasyprint import HTML
from flask import Flask, render_template_string
from flask_sqlalchemy import SQLAlchemy
from models import *
from models import Theatre
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ticket_show.sqlite3'

db.init_app(app)
with app.app_context():
    db.create_all()

template_string = """
<!doctype html>
<html>
  <head>
    <style>
      /* CSS styles for the PDF report */
      body {
        font-family: Arial, sans-serif;
        padding: 20px;
      }
      
      h1 {
        color: #333;
        text-align: center;
      }
      
      ul {
        list-style-type: none;
        padding: 0;
        margin: 0;
      }
      
      li {
        margin-bottom: 10px;
      }
      
      .admin-details {
        margin-bottom: 30px;
      }
      
      .theatre-list {
        margin-top: 40px;
      }
      
      .theatre-item {
        margin-bottom: 20px;
        border: 1px solid #ddd;
        padding: 10px;
      }
      
      .theatre-name {
        font-size: 18px;
        font-weight: bold;
      }
      
      .theatre-place {
        color: #555;
        font-size: 14px;
      }
      
      .theatre-location {
        font-size: 14px;
      }
      
      .theatre-capacity {
        font-size: 14px;
      }
      
      .show-list {
        margin-top: 20px;
      }
      
      .show-item {
        margin-bottom: 10px;
        border: 1px solid #ddd;
        padding: 5px;
      }
      
      .show-name {
        font-size: 14px;
        font-weight: bold;
      }
      
      .show-rating {
        color: #555;
        font-size: 12px;
      }
      
      .show-timings {
        font-size: 12px;
      }
      
      .show-price {
        font-size: 12px;
      }
      
      .show-tags {
        font-size: 12px;
      }
      
      /* Add your custom CSS styles here */
    </style>
  </head>
  <body>
    <h1>Admin: {{ admin.name }}</h1>
    
    <div class="admin-details">
      <ul>
        <h3> Please view your details below</h3>
      </ul>
    </div>
    
    <div class="theatre-list">
      <h2>Theatre Details</h2>
      {% for theatre in admin.theatres %}
        <div class="theatre-item">
          <div class="theatre-name">{{ theatre.venue_name }}</div>
          <div class="theatre-place">Place: {{ theatre.place }}</div>
          <div class="theatre-location">Location: {{ theatre.location }}</div>
          <div class="theatre-capacity">Capacity: {{ theatre.capacity }}</div>
          
          <div class="show-list">
            <h3>Show Details</h3>
            {% for show in theatre.shows %}
              <div class="show-item">
                <div class="show-name">{{ show.show_name }}</div>
                <div class="show-rating">Ratings: {{ show.ratings }}</div>
                <div class="show-timings">Timings: {{ show.timings }}</div>
                <div class="show-price">Price: {{ show.price }}</div>
                <div class="show-tags">Tags: {{ show.tags }}</div>
              </div>
            {% endfor %}
          </div>
        </div>
      {% endfor %}
    </div>
    
  </body>
</html>
"""

def format_report(admin):
    template = Template(template_string)
    return template.render(admin=admin)

def create_pdf_report(admin, filename):
    html = render_template_string(format_report(admin))
    pdf_path = os.path.join('pdf_reports', filename)
    HTML(string=html).write_pdf(pdf_path)
    print(f"PDF report has been created: {pdf_path}")

if __name__ == '__main__':
    with app.app_context():
        pdf_reports_dir = 'pdf_reports'
        os.makedirs(pdf_reports_dir, exist_ok=True)
        admins = Admin.query.all()
        print(f"Number of admins: {len(admins)}")
        for admin in admins:
            filename = f"Admin.{admin.name}.pdf"
            print(f"Generating PDF for admin: {admin.name}")
            create_pdf_report(admin, filename)
