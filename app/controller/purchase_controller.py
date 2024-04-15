from flask import Blueprint
from flask_restx import Namespace, Resource, fields

from domain.entity.entity import PurchaseOrder
from domain.repository.purchase_repository import create_purchase_order, update_purchase_order, delete_purchase_order, \
    read_all_purchase_orders
from gateways.connection import session

purchase_order_controller = Blueprint('purchase_order', __name__)
purchase_order_ns = Namespace('purchase_order', description='Operações relacionadas a pedidos de compra')

purchase_order_model = purchase_order_ns.model('PurchaseOrder', {
    'id': fields.Integer(readonly=True, description='ID do pedido de compra'),
    'user_id': fields.Integer(required=True, description='ID do usuário'),
    'food_id': fields.Integer(required=True, description='ID do alimento'),
    'date': fields.Date(required=True, description='Data do pedido'),
    'status': fields.String(required=True, description='Status do pedido')
})


@purchase_order_ns.route('')
class PurchaseOrdersController(Resource):
    @purchase_order_ns.doc('list_purchase_orders')
    @purchase_order_ns.marshal_list_with(purchase_order_model)
    def get(self):
        purchase_orders = read_all_purchase_orders()
        return purchase_orders

    @purchase_order_ns.doc('create_purchase_order')
    @purchase_order_ns.expect(purchase_order_model)
    def post(self):
        data = purchase_order_ns.payload
        create_purchase_order(**data)
        return {'message': 'Pedido de compra criado com sucesso'}, 201


@purchase_order_ns.route('/<int:purchase_order_id>')
@purchase_order_ns.param('purchase_order_id', 'ID do pedido de compra')
class PurchaseOrderController(Resource):
    @purchase_order_ns.doc('update_purchase_order')
    @purchase_order_ns.expect(purchase_order_model)
    def put(self, purchase_order_id):
        data = purchase_order_ns.payload
        update_purchase_order(purchase_order_id, **data)
        return {'message': 'Pedido de compra atualizado com sucesso'}, 200

    @purchase_order_ns.doc('delete_purchase_order')
    def delete(self, purchase_order_id):
        delete_purchase_order(purchase_order_id)
        return {'message': 'Pedido de compra excluído com sucesso'}, 200


purchase_order_ns.marshal_with(purchase_order_controller)
