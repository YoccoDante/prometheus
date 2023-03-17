# blueprints/basic_endpoints/__init__.py
from flask import Blueprint, request, make_response
from datetime import datetime, timedelta

import jwt

bpAuth = Blueprint('user', __name__, url_prefix='/auth')


@bpAuth.route('/login', methods=['POST'])
def login():
    auth = request.json
    if not auth or not auth.get('password') or not auth.get('username'):
        return make_response({"message": "User or password missing"}, 400)
    if auth.get('username') == 'Pedro' and auth.get('password') == '123':
        token = jwt.encode({
            'public_id': '1',
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }, 'ENTROPY')
        return make_response({'username': auth.get('username'), 'token': token}, 201)
    return make_response({"message": "Usuario or password are invalid"}, 401)
