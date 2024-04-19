from flask import Blueprint, request, jsonify
from flask_restx import fields, Namespace, Resource
from werkzeug.security import check_password_hash
from domain.repository.user_repository import read_user_by_email, read_password_by_email

login_controller = Blueprint('login', __name__)
login_ns = Namespace('login', description='Operações relacionadas a login')

login_model = login_ns.model('Login', {
    'email': fields.String(required=True, description='E-mail do usuário'),
    'password': fields.String(required=True, description='Senha do usuário'),
})


@login_ns.route('')
class LoginController(Resource):

    @login_ns.doc('login')
    @login_ns.expect(login_model)
    def post(self):
        data = request.json
        email = data.get('email')
        password = data.get('password')

        user = read_user_by_email(email)
        password_hash = read_password_by_email(email)
        print(password_hash)
        print(password)

        if user and password_hash and check_password_hash(password_hash, password):
            return {'message': 'Login successful', 'user_id': user.id}, 200
        else:
            return {'message': 'Invalid email or password'}, 401
