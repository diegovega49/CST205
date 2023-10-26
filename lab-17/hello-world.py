'''
Diego Vega
CST 205
Lab 17
'''

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

# Task 2
@app.route('/')
def hello():
    header = '<h1><span style = color:red;> Hello world!</span></h1>'
    p1 = '<p>Diego : LOL</P>'
    return header + p1

# Task 3
@app.route('/diego')
def t_test():
    return render_template('template.html')

