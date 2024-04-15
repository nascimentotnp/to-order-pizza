from flask import Blueprint
from flask_restx import Namespace, Resource, fields

from domain.repository.pizza_repository import create_pizza, read_pizza_by_id, update_pizza, \
    delete_pizza, read_active_pizzas

pizza_controller = Blueprint('pizza', __name__)
pizza_ns = Namespace('pizza', description='Operações relacionadas a pizzas')

pizza_model = pizza_ns.model('Pizza', {
    'id': fields.Integer(readonly=True, description='ID da pizza'),
    'name': fields.String(required=True, description='Nome da pizza'),
    'price': fields.Float(required=True, description='Preço da pizza'),
    'filling': fields.String(required=True, description='Recheio da pizza'),
    'size': fields.String(required=True, description='Tamanho da pizza'),
    'stuffed_pizza_edge': fields.Boolean(description='Borda recheada'),
    'flavor_stuffed_pizza_edge': fields.String(description='Sabor da borda recheada')
})


@pizza_ns.route('/<int:pizza_id>')
@pizza_ns.param('pizza_id', 'ID da pizza')
class PizzaController(Resource):
    @pizza_ns.doc('get_pizza')
    @pizza_ns.marshal_with(pizza_model)
    def get(self, pizza_id):
        pizza = read_pizza_by_id(pizza_id)
        if pizza:
            return pizza
        else:
            pizza_ns.abort(404, message='Pizza não encontrada')

    @pizza_ns.doc('update_pizza')
    @pizza_ns.expect(pizza_model)
    def put(self, pizza_id):
        data = pizza_ns.payload
        update_pizza(pizza_id, **data)
        return {'message': 'Pizza atualizada com sucesso'}, 200

    @pizza_ns.doc('delete_pizza')
    def delete(self, pizza_id):
        delete_pizza(pizza_id)
        return {'message': 'Pizza excluída com sucesso'}, 200


@pizza_ns.route('')
class PizzaController(Resource):
    @pizza_ns.doc('create_pizza')
    @pizza_ns.expect(pizza_model)
    def post(self):
        data = pizza_ns.payload
        create_pizza(**data)
        return {'message': 'Pizza criada com sucesso'}, 201

    @pizza_ns.doc('get_pizzas')
    @pizza_ns.marshal_list_with(pizza_model)
    def get(self):
        pizzas = read_active_pizzas()
        return pizzas


pizza_ns.marshal_with(pizza_controller)
