from flask_login import login_required
from app import app
from flask import render_template

# This is for rendering the home page
@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

