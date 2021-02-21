from flask import Flask, render_template


# the app needs a unique name, and __name__ is always unique
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")
