from flask import Flask
from flask_cors import CORS
from flask_restx import Api

from controller.pasta_controller import pasta_controller, pasta_ns
from controller.pizza_controller import pizza_controller, pizza_ns


app = Flask(__name__)
CORS(app, origins="*")
api = Api(app, version='1.0', title='To order restaurant', url_scheme='http://localhost:8080/docs',
          description='Documentação API para MVP', doc="/docs")
api.add_namespace(pizza_ns)
api.add_namespace(pasta_ns)

app.register_blueprint(pizza_controller)
app.register_blueprint(pasta_controller)

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
