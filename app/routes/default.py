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
    
@app.route('/homeDefs')
def homeDefs():
    return render_template('homeDefs.html')

@app.route('/posts')
def posts():
    return render_template('posts.html')

@app.route('/userhome')
def userhome():
    return render_template('userhome.html')

@app.route('/form_homeDef')
def form_homeDef():
    return render_template('form_homeDef.html')

@app.route('/home_collection')
def home_collection():
    return render_template('home_collection.html')