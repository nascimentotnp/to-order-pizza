from flask import Flask
from flask_restx import Api

from controller.pasta_controller import pasta_controller, pasta_ns
from controller.pizza_controller import pizza_controller, pizza_ns
from controller.purchase_controller import purchase_order_controller, purchase_order_ns
from controller.user_controller import user_controller, user_ns

app = Flask(__name__)

api = Api(app, version='1.0', title='To order restaurant', url_scheme='http://localhost:8080/docs',
          description='Documentação API para MVP', doc="/docs")
api.add_namespace(user_ns)
api.add_namespace(pizza_ns)
api.add_namespace(pasta_ns)
api.add_namespace(purchase_order_ns)


app.register_blueprint(user_controller)
app.register_blueprint(pizza_controller)
app.register_blueprint(pasta_controller)
app.register_blueprint(purchase_order_controller)


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)


