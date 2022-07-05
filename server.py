from flask import Flask, request, jsonify
from module.database import Database

app  = Flask(__name__)
db = Database()

@app.route('/')
def index():
    return "Hola mundo"

@app.route("/readhechos")
def readhechos():
    if request.method == 'GET':
        try:
            result = db.readhechos(request.json["id"])
        except Exception as e:
            return e
    return jsonify(result)

@app.route("/readproductos")
def readproductos():
    if request.method == 'GET':
        try:
            result = db.readproductos(request.json["id"])
        except Exception as e:
            return e
    return jsonify(result)

@app.route("/readclientes")
def readclientes():
    if request.method == 'GET':
        try:
            result = db.readclientes(request.json["id"])
        except Exception as e:
            return e
    return jsonify(result)

@app.route("/readProductosMasVendidoCat")
def readProductosMasVendidoCat():
    if request.method == 'GET':
        try:
            result = db.readProductosMasVendidoCategori(request.json["name_cat"])
        except Exception as e:
            return e
    return jsonify(result)

if __name__ == "__main__":
    app.debug = True
    app.run()

