from flask import Flask, render_template
from cs50 import SQL
import math
import random
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import io
import base64


app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True
# add db file
db = SQL("sqlite:///collections.db")


collections_count = db.execute('SELECT COUNT(*) FROM collections')
total = collections_count[0]['COUNT(*)']
max_page = math.ceil(total / 12)


@app.route("/")
def home():
    rand_ids = random.sample(range(1, total + 1), 3)
    rand_collections = db.execute('SELECT * FROM collections WHERE id in (?)', tuple(rand_ids))
    return render_template("index.html", rand_collections=rand_collections)

@app.route("/data")
def get_data():
    museum_count = db.execute('SELECT museum, COUNT(*) as count FROM collections GROUP BY museum')
    data = {}
    for museum in museum_count:
        data[museum['Museum']] = museum['count']
    labels = list(data.keys())
    values = list(data.values())
    
    plt.figure(figsize=(12, 6))
    plt.bar(labels, values)

    plt.title('Open Access Chinese Art Collections in US Art Museums')
    plt.xlabel('Museum Name')
    plt.ylabel('Number of Art')

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    chart = base64.b64encode(img.getvalue()).decode()
    return render_template('data.html', chart=chart)

   

def get_collections(offset=0):
    my_collection = db.execute('SELECT * FROM collections LIMIT 12 OFFSET ?', offset)
    return my_collection


@app.route('/collections')
def collections():
    collections=get_collections()
    page=1
    return render_template("collections.html", collections=collections, page=page)


@app.route('/collections/<string:id>')
def collections_paginate(id):
    int_id = int(id)
    if int_id > max_page or int_id < 1 or id[0] == "0":
        return render_template("error.html")
    else:
        offset = (int_id - 1) * 12
        collections=get_collections(offset)
        return render_template("collections.html", collections=collections, page=int_id)

@app.route('/collections/art/<string:art_id>')
def get_art(art_id):
     int_art = int(art_id)
     if int_art > total or int_art < 1 or art_id[0] == "0":
        return render_template("error.html")
     else:
         art = db.execute('SELECT * FROM collections WHERE id = ?', art_id)
         return render_template("art.html", collections=collections, art=art)



