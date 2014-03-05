'''
Created on Mar 5, 2014

@author: karol
'''
from flask import Flask, request
from werkzeug import redirect
from flask.templating import render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/~average-joe/welcome/')
def welcome():
    return render_template('welcome.html')


@app.route('/~average-joe/', methods=['GET', 'POST'])
def login1():
    if request.method == 'POST':  # @UndefinedVariable
        return redirect('/~average-joe/welcome/')
    else:
        return render_template('vanilla.html')


@app.route('/~mr-hacker/', methods=['GET', 'POST'])
def login2():
    if request.method == 'POST':  # @UndefinedVariable
        return redirect('/')
    else:
        return render_template('injected.html')

if __name__ == '__main__':
    app.run(debug=True)