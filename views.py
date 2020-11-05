from app import app
from flask import render_template, request

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create_auto', methods=["POST", "GET"])
def create_auto():
    context = None
    if request.method == "POST":
        auto_title = request.form['title']
        auto_price = request.form['price']
        context = {
            'method': 'POST',
            'title': auto_title,
            'price': auto_price,
        }
    elif request.method == "GET":
        context = {
            'method': "GET"
        }
    return render_template('create_auto.html', **context)