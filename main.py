from flask_bootstrap import Bootstrap4
from flask import Flask

app = Flask(__name__)

bootstrap = Bootstrap4(app)

app.route('/page1.html')
def wc():
   s1 = 'Welcome to my page! '
   s2 = 'Have a nice day!'
   return s1 + s2