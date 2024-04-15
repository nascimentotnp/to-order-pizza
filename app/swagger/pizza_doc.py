# from flask import jsonify, request
# from flask_restx import Resource, Namespace
#
# from controller.dto.pizza_dto import PizzaDTO
# from domain.repository.pizza_repository import (
#     create_pizza,
#     read_all_pizzas,
#     read_pizza_by_id,
#     update_pizza,
#     delete_pizza
# )
#
# swagger_pizza = Namespace('pizzas')
#
#
# @swagger_pizza.route('/pizzas')
# class PizzasSwagger(Resource):
#     @swagger_pizza.doc()
#     def get(self):
#         """
#         Get all pizzas.
#         """
#         pizzas = read_all_pizzas()
#         return jsonify([pizza.serialize() for pizza in pizzas])
#
#     @swagger_pizza.doc(params={'pizza_id': 'Pizza ID'})
#     def get_by_id(self, pizza_id):
#         """
#         Get pizza by ID.
#         """
#         pizza = read_pizza_by_id(pizza_id)
#         if pizza:
#             return jsonify(pizza.serialize()), 200
#         else:
#             return jsonify({'error': 'Pizza not found'}), 404
#
#     @swagger_pizza.doc(params={
#         'name': 'Name of the pizza',
#         'price': 'Price of the pizza',
#         'filling': 'Filling of the pizza',
#         'size': 'Size of the pizza',
#         'stuffed_pizza_edge': 'Whether the pizza has stuffed edge',
#         'flavor_stuffed_pizza_edge': 'Flavor of the stuffed edge'
#     }, responses={201: 'Created', 400: 'Bad Request'})
#     def post(self):
#         """
#         Create a new pizza.
#         """
#         data = request.json
#         pizza_dto = PizzaDTO(**data)
#
#         if not pizza_dto.name or not pizza_dto.price or not pizza_dto.filling or not pizza_dto.size:
#             return jsonify({'error': 'Please provide all necessary fields'}), 400
#
#         create_pizza(
#             name=pizza_dto.name,
#             price=pizza_dto.price,
#             filling=pizza_dto.filling,
#             size=pizza_dto.size,
#             stuffed_pizza_edge=pizza_dto.stuffed_pizza_edge,
#             flavor_stuffed_pizza_edge=pizza_dto.flavor_stuffed_pizza_edge
#         )
#
#         return jsonify({'message': 'Pizza created successfully'}), 201
#
#     @swagger_pizza.doc(params={'pizza_id': 'Pizza ID'}, responses={200: 'OK', 400: 'Bad Request', 404: 'Not Found'})
#     def put(self, pizza_id):
#         """
#         Update pizza by ID.
#         """
#         pizza = read_pizza_by_id(pizza_id)
#         if not pizza:
#             return jsonify({'error': 'Pizza not found'}), 404
#
#         data = request.json
#         update_pizza(pizza_id, **data)
#         return jsonify({'message': 'Pizza updated successfully'}), 200
#
#     @swagger_pizza.doc(params={'pizza_id': 'Pizza ID'}, responses={200: 'OK', 404: 'Not Found'})
#     def delete(pizza_id):
#         """
#         Delete pizza by ID.
#         """
#         pizza = read_pizza_by_id(pizza_id)
#         if not pizza:
#             return jsonify({'error': 'Pizza not found'}), 404
#
#         delete_pizza(pizza_id)
#         return jsonify({'message': 'Pizza deleted successfully'}), 200
