from flask import Flask, render_template
from cs50 import SQL

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

# add db file
db = SQL("sqlite:///art.db")

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")
