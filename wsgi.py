# wsgi.py
from flask import Flask, jsonify, request, abort
app = Flask(__name__)

PRODUCTS = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
    3: { 'id': 3, 'name': 'Le Wagon'},
}

class Counter:
    def __init__(self):
        self.id = len(list(PRODUCTS))

    def next(self):
        self.id += 1
        return self.id

ID = Counter()

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products')
def read_many_products():
    products = list(PRODUCTS.values())
    return jsonify(products), 200

@app.route('/api/v1/products/<int:id>')
def read_single_product(id):
    product = PRODUCTS.get(id)
    if product is None:
        abort(404)
    return jsonify(product), 200

@app.route('/api/v1/products/<int:id>', methods=['DELETE'])
def delete_single_product(id):
    removed_product = PRODUCTS.pop(id, None)
    if removed_product is None:
        abort(404)
    return "", 204  #contenu d'une réponse est du texte, d'ou la chaine vide

@app.route('/api/v1/products', methods=['POST'])
def create_single_product():
    data = request.get_json()
    name = data.get("name") #ou data["name"] erreur si key non touvé dans le dict

    if name is None:
        abort(400)

    new_id = ID.next()

    PRODUCTS[new_id] = {'id': new_id, 'name': name}

    return jsonify(PRODUCTS[new_id]), 201

@app.route('/api/v1/products<int:id>', methods=['PATCH'])
def update_single_product():
    data = request.get_json()
    name = data.get("name") #ou data["name"] erreur si key non touvé dans le dict
    if name is None:
        abort(422)

    PRODUCTS[id] = {'id': id, 'name': name}

    return jsonify(PRODUCTS[id]), 204

