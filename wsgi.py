# wsgi.py
from flask import Flask, jsonify
app = Flask(__name__)

PRODUCTS = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
    3: { 'id': 3, 'name': 'Le Wagon'},
}

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products')
def read_many_products():
    products = list(PRODUCTS.values())
    return jsonify(products), 200

@app.route('/api/v1/products/:', PRODUCTS.id())
def read_product():
    product = str(PRODUCTS.values(id))
    return jsonify(product), 200
