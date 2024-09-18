from flask import jsonify, current_app
from flask import Blueprint
from flask import Flask, render_template, request, jsonify
from sqlalchemy import func

from models.Names import Names

bp = Blueprint('routes', __name__)

@app.route("/")
def main():
    return render_template('foryou.html')


@app.route("/search", methods=['POST', 'GET'])
async def search():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        data_db = await Select(data.get('search'))
        rez = [
            {
                'id': i[0],
                'name': i[1],
                'price': i[2],
                'color': i[3],
                'specification': i[4]
            } for i in data_db
        ]
        print(rez)
        return jsonify(rez)
    return render_template('search.html')


@app.route("/device", methods=['POST', 'GET'])
async def devise():
    return render_template('device.html')


@app.route("/delivery", methods=['POST', 'GET'])
async def delivery():
    return render_template('delivery.html')


@app.route("/trade-in", methods=['POST', 'GET'])
async def trade_in():
    return render_template('trade-in.html')


@bp.route("/name")
def name():
    n = Names.query.order_by(func.random()).first()
    return jsonify({"names" : "%s = %d" % (n.name, n.amount) })

# http://azzrael_code.yt/add_random
@bp.route("/add_random")
def add_random():
    n = Names()
    n.fill_random()
    n.save()
    return jsonify({"added" : "%s = %d" % (n.name, n.amount)})