from unicodedata import name
from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
@app.route('/index/<name>')
def index():
    text="Hello World!!!"
    return render_template("index html)", text=name)

@app.route('/extract')
