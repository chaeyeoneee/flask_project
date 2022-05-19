from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/myinfo")
def myinfo():
    return render_template("myinfo.html")
