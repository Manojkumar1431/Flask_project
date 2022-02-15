from datetime import datetime
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to my flash cards application!"
'''
@app.route("/date")
def date():
    return "This page was served at "+str(datetime.now())

counter = 0
@app.route("/no of visits")
def count():
    global counter
    counter += 1
    return "So far "+str(counter)+" members visited the site"
'''
@app.route("/welcome")
def portfolio():
    return render_template('welcome.html', name="mintu")