from flask import Flask, request, render_template, url_for
from markupsafe import escape
import os
import flask_class as fc


app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name", "world")
    return render_template("index.html", placeholder=name)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/user")
def show_user_profile():
    print(os.getlogin())
    return f'User {escape(os.getlogin())}'

@app.route("/cabinet_entry")
def cabinet_entry():
    return render_template('cabinet.html')

if __name__ == "__main__":
    app.run(debug=True)
