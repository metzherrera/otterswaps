from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

# Sample data for listings
listings = [
    {'title': 'Coffee pot, like new', 'price': '$10', 'description': 'A fairly new, gently used coffee pot.'},
    {'title': 'Green mountain bike', 'price': '$20', 'description': 'Heavily used mountain bike. Some paint is chipped but runs like new.'},
    {'title': 'SAW III Collectible mug', 'price': '$15', 'description': 'Please take this off my hands. Comes with the box.'}
]


@app.route('/')
def index():
    return render_template('index.html', listings=listings)


if __name__ == '__main__':
    app.run(debug=True)
