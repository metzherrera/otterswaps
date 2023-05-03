from flask_bootstrap import Bootstrap5
from flask import Flask, render_template

app = Flask(__name__)

bootstrap = Bootstrap5(app)

@app.route('/mytemplate')
def t_test():
   return render_template('page1.html')



@app.route('/userlogin')
def t_test():
   return render_template('page2.html')