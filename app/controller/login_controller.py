from flask import render_template, Blueprint
from flask_restx import Namespace, Resource, fields

login_controller = Blueprint('login', __name__)
login_ns = Namespace('login', description='Operações relacionadas a pizzas')


def login():
    pass
