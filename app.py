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

@app.post("/upload") 
def upload():
    if "photo" in request.files:
        filename = photos.save(request.files["photo"])
        flash("Photo saved successfully.")
        return redirect(url_for("display_image", filename=filename))

@app.route("/display/<filename>")
def display_image(filename):
    return render_template("home.html", filename=filename)

@app.get("/create")
def index():
    return render_template("upload.html")

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


# @app.route('/')
# def index():
#     return render_template('index.html')

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
            # Set the user as authenticated in the session
            session['user'] = user[0]
            return redirect('/create')
        else:
            flash('Invalid username or password')
    
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)