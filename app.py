from flask import Flask, request, render_template
from markupsafe import escape
import os

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name", "world")
    return render_template("index.html", placeholder=name)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route(f"/user")
def show_user_profile():
    print(os.getlogin())
    return f'User {escape(os.getlogin())}'

if __name__ == "__main__":
    app.run(debug=True)
