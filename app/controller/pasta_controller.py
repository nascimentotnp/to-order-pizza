from flask import Blueprint
from flask_restx import Namespace, Resource, fields

from domain.repository.pasta_repository import create_pasta, read_all_pastas, read_pasta_by_id, \
    update_pasta, delete_pasta, read_active_pastas

pasta_controller = Blueprint('pasta', __name__)
pasta_ns = Namespace('pasta', description='Operações relacionadas a pastas')

pasta_model = pasta_ns.model('Pasta', {
    'id': fields.Integer(readonly=True, description='ID da pasta'),
    'name': fields.String(required=True, description='Nome da pasta'),
    'price': fields.Float(required=True, description='Preço da pasta'),
    'filling': fields.String(required=True, description='Recheio da pasta'),
    'pasta_type': fields.String(required=True, description='Tipo de massa da pasta'),
    'sauce_type': fields.String(required=True, description='Tipo de molho da pasta')
})


@pasta_ns.route('/<int:pasta_id>')
@pasta_ns.param('pasta_id', 'ID da pasta')
class PastaController(Resource):
    @pasta_ns.doc('get_pasta')
    @pasta_ns.marshal_with(pasta_model)
    def get(self, pasta_id):
        pasta = read_pasta_by_id(pasta_id)
        if pasta:
            return pasta
        else:
            pasta_ns.abort(404, message='Pasta não encontrada')

    @pasta_ns.doc('update_pasta')
    @pasta_ns.expect(pasta_model)
    def put(self, pasta_id):
        data = pasta_ns.payload
        update_pasta(pasta_id, **data)
        return {'message': 'Pasta atualizada com sucesso'}, 200

    @pasta_ns.doc('delete_pasta')
    def delete(self, pasta_id):
        delete_pasta(pasta_id)
        return {'message': 'Pasta excluída com sucesso'}, 200


@pasta_ns.route('')
class PastaController(Resource):
    @pasta_ns.doc('create_pasta')
    @pasta_ns.expect(pasta_model)
    def post(self):
        data = pasta_ns.payload
        create_pasta(**data)
        return {'message': 'Pasta criada com sucesso'}, 201

    @pasta_ns.doc('get_pastas')
    @pasta_ns.marshal_list_with(pasta_model)
    def get(self):
        pastas = read_active_pastas()
        return pastas


pasta_ns.marshal_with(pasta_controller)
