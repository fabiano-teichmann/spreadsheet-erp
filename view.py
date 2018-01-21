from flask import Flask, jsonify, request
import json
from models import Produto
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1> HELLO WORD </h1>"


@app.route('/produtos')
def produtos():
    #list comprehension
    return jsonify([produto.to_dict() for produto in Produto.select()])

@app.route('/produto/<int:id_produto>')
def produto(id_produto):
    try:
        produto = Produto.get(id=id_produto)
        return jsonify(produto.to_dict())
    except Produto.DoesNoExist:
        return jsonify({'status': 404, 'msg': 'Product not found'}), 404
@app.route('/produto', methods=['POST'])
def new_product():
    dados = request.json
    produto = Produto(name=dados['name'], description=dados['description'], 
    stock=dados['stock'], price=dados['stock'])

    produto.save()
    return jsonify({'status': 200, 'msg': 'Save Sucess!'}),200




if __name__ == '__main__':
    app.run(debug=True) 