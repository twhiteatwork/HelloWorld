from flask import Flask
from markupsafe import escape

app = Flask(__name__)

#To run app, from folder at command prompt "flask --app FlaskQuickstart run" and browse provided link
#Alternatively, name file app.py or wsgi.py, --app not required, at command prompt can simply "flask run" and browse provided link
#Add --debug parameter to get detailed debug output
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#<name> is a variable passed into function
@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"