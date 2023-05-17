from flask import Flask, render_template, request, redirect, g, session, flash, url_for
from flask_uploads import IMAGES, UploadSet, configure_uploads
import sqlite3

app = Flask(__name__)
DATABASE = 'database.db'
# app.secret_key = 'your_secret_key'
photos = UploadSet("photos", IMAGES)
app.config["UPLOADED_PHOTOS_DEST"] = "static/images"
app.config["SECRET_KEY"] = "mysecretkey"
configure_uploads(app,photos)
# functions for setting up database, opening, saving, closing properly - Metztli
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/upload", methods=['POST'])
def upload():
    if "photo" in request.files:
        filename = photos.save(request.files["photo"])
        description = request.form['description']
        save_image_description(filename, description)
        flash("Photo and description saved successfully.")
    return redirect("/listings")

@app.route("/display/<filename>")
def display_image(filename):
    return render_template("home.html", filename=filename)

@app.route("/create", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        description = request.form['description']
        flash("Description saved successfully.")
    return render_template("create.html")


# login and signup pages, created and designed with a template from Bootstrap - Jennesae
# functionality for saving text in fields to sql database - Metztli
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        db = get_db() # Save username and password into database
        cursor = db.cursor()
        cursor.execute('INSERT INTO users (email, password) VALUES (?, ?)',
                       (username, password))
        db.commit()
        return redirect('/login')
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users WHERE email = ?', (username,))
        user = cursor.fetchone()

        if user and user[2] == password:
            session['user'] = user[0]
            return redirect('/create')
        else:
            flash('Invalid username or password')
    
    return render_template('login.html')

# Page to display listings - Hannah
@app.route("/listings")
def display_images():
    image_data = get_image_data()
    return render_template("listings.html", image_data=image_data)

# Functions to serialize listing data in database - Metztli
def save_image_description(filename, description):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO images (filename, description) VALUES (?, ?)', (filename, description))
        conn.commit()

def get_image_data():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT filename, description FROM images')
        rows = cursor.fetchall()
        image_data = [{'filename': row[0], 'description': row[1]} for row in rows]
        return image_data

if __name__ == '__main__':
    app.run(debug=True)
