from flask import Flask, escape, request


'''
http://flask.palletsprojects.com/en/1.1.x/

#under cmd of windows10
set FLASK_APP=demo_flask.py
flask run
#http://localhost:5000/?name=bill

'''
app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'