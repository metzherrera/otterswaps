from flask import Flask, request, redirect, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def page0():
    return render_template('index.html')

@app.route('/login')
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
    return render_template('login.html')