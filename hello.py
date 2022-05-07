from flask import Flask, render_template
app = Flask(__name__)

import mariadb 
import sys
sys.path.insert(0, '/home/vishal')
import detail


conn = mariadb.connect(
    user = detail.username,
    password = detail.password,
    host="localhost",
    database = detail.database)
cur = conn.cursor()

@app.route('/')
def example():
    cur.execute("SELECT Name FROM Mentor")
    data = cur.fetchall()
    return render_template('index.html', output = data) 

# @app.route('/')
# def hello_world():
#     return 'Hello World!'
