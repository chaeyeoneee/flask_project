from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/myinfo")
def myinfo():
    return render_template("myinfo.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/login")
def login():
    return render_template("login.html")
