from flask import Flask, request, redirect, render_template, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def page0():
    return render_template('page1.html')

@app.route('/login')
def page1():
    return render_template('login.html')

@app.route('/signup')
def page2():
    return render_template('signup.html')