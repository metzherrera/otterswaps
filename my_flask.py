import os
from flask import Flask, flash, request, redirect, render_template, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename
import sqlite3

app = Flask(__name__)
# bootstrap = Bootstrap5(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def page1():
    return render_template('login.html')

@app.route('/signup')
def page2():
    return render_template('signup.html')

