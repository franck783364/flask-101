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

@app.route('/api/v1/products/:<int:id>')
def read_single_product(id):
    product = PRODUCTS.get(id)
    return jsonify(product), 200

@app.route('/api/v1/products/:<int:id>', methods=['DELETE'])
def delete_single_product(id):
    PRODUCTS = PRODUCTS.remove(id)
    return NULL, 204
