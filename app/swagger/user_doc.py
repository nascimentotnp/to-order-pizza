from flask import jsonify, request
from flask_restx import Resource, Namespace
from domain.repository.user_repository import (
    create_user,
    read_all_users,
    read_user_by_email,
    read_user_by_id,
    update_user,
    delete_user
)

swagger_user = Namespace('users')


@swagger_user.route('/')
class UsersController(Resource):
    @swagger_user.doc()
    def get(self):
        """
        Get all users.
        """
        users = read_all_users()
        return jsonify([user.serialize() for user in users])

    @swagger_user.doc(params={'user_id': 'User ID'})
    def get_by_id(self, user_id):
        """
        Get user by ID.
        """
        user = read_user_by_id(user_id)
        if user:
            return jsonify(user.serialize()), 200
        else:
            return jsonify({'error': 'User not found'}), 404

    @swagger_user.doc(params={'email': 'Email'})
    def get_by_email(self):
        """
        Get user by Email.
        """
        email = request.args.get('email')
        user = read_user_by_email(email)
        if user:
            return jsonify(user.serialize()), 200
        else:
            return jsonify({'error': 'User not found'}), 404

    @swagger_user.doc(responses={201: 'Created', 400: 'Bad Request', 409: 'Conflict'})
    def post(self):
        """
        Create a new user.
        """
        data = request.json
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        if not name or not email or not password:
            return jsonify({'error': 'Please provide all required fields'}), 400

        if read_user_by_email(email):
            return jsonify({'error': 'User already exists'}), 409

        create_user(name, email, password)
        return jsonify({'message': 'User created successfully'}), 201

    @swagger_user.doc(params={'user_id': 'User ID'}, responses={200: 'OK', 400: 'Bad Request', 404: 'Not Found'})
    def put(self, user_id):
        """
        Update user by ID.
        """
        user = read_user_by_id(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        data = request.json
        update_user(user_id, **data)
        return jsonify({'message': 'User updated successfully'}), 200

    @swagger_user.doc(params={'user_id': 'User ID'}, responses={200: 'OK', 404: 'Not Found'})
    def delete(self, user_id):
        """
        Delete user by ID.
        """
        user = read_user_by_id(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        delete_user(user_id)
        return jsonify({'message': 'User deleted successfully'}), 200
