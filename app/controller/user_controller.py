from flask import Blueprint
from flask_restx import Namespace, Resource, fields

from domain.entity.entity import User
from domain.repository.user_repository import read_user_by_id, create_user, read_all_users, update_user, delete_user, \
    read_active_users, read_user_by_email
from gateways.connection import session
from gateways.database import save

user_controller = Blueprint('user', __name__)
user_ns = Namespace('user', description='Operações relacionadas a usuários')

user_model = user_ns.model('User', {
    'id': fields.Integer(readonly=True, description='ID do usuário'),
    'name': fields.String(required=True, description='Nome do usuário'),
    'email': fields.String(required=True, description='E-mail do usuário'),
    'password': fields.String(required=True, description='Senha do usuário'),
    'active': fields.Boolean(required=True, description='Usuário ativo ou inativo')
})


@user_ns.route('')
class UsersController(Resource):
    @user_ns.doc('list_users')
    @user_ns.marshal_list_with(user_model)
    def get(self):
        users = read_active_users()
        return users

    @user_ns.doc('create_user')
    @user_ns.expect(user_model)
    def post(self):
        data = user_ns.payload
        existing_user = read_user_by_email(data['email'])
        if existing_user:
            return {'error': 'Este email já está em uso'}, 400
        else:
            create_user(**data)
            return {'message': 'Usuário criado com sucesso'}, 201


@user_ns.route('/<int:user_id>')
@user_ns.param('user_id', 'ID do usuário')
class UserController(Resource):
    @user_ns.doc('get_user')
    @user_ns.marshal_with(user_model)
    def get(self, user_id):
        user = read_user_by_id(user_id)
        if user:
            return user
        else:
            user_ns.abort(404, message='Usuário não encontrado')

    @user_ns.doc('update_user')
    @user_ns.expect(user_model)
    def put(self, user_id):
        data = user_ns.payload
        update_user(user_id, **data)
        return {'message': 'Usuário atualizado com sucesso'}, 200

    @user_ns.doc('delete_user')
    def delete(self, user_id):
        delete_user(user_id)
        return {'message': 'Usuário excluído com sucesso'}, 200


user_ns.marshal_with(user_controller)
