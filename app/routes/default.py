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

@app.route('/challenge')
def challenge():
    return render_template('challenge.html')
    
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/sharehome')
def sharehome():
    return render_template('sharehome.html')

@app.route('/userhome')
def userhome():
    return render_template('userhome.html')