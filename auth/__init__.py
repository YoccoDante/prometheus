# blueprints/basic_endpoints/__init__.py
from flask import Blueprint, request

bpAuth = Blueprint('user', __name__, url_prefix='/auth')


@bpAuth.route('/login', methods=['POST'])
def login():
        return {
            "user": "Pedro"
        }
