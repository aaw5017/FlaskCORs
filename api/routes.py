from flask import Blueprint, request, make_response
api_bp = Blueprint('api', __name__, url_prefix='/api')

def get_cors_headers(method: str):
    return {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': f'{str.upper(method)}, OPTIONS',
        'Access-Control-Allow-Origin': 'http://localhost:9000'
    }

@api_bp.route('/')
def index():
    return 'Index hit'

@api_bp.route('/post-test', methods=['POST', 'OPTIONS'])
def post_test():
    headers = get_cors_headers('POST')

    if request.method == 'OPTIONS':
        return make_response(('', 204, headers))

    return make_response(({'data': 'hey now, you POST-ed'}, 200, headers))

@api_bp.route('/put-test', methods=['PUT', 'OPTIONS'])
def put_test():
    headers = get_cors_headers('PUT')

    if request.method == 'OPTIONS':
        return make_response(('', 204, headers))

    return make_response(({'data': 'hey now, you PUT-ed'}, 200, headers))

@api_bp.route('/delete-test', methods=['DELETE', 'OPTIONS'])
def delete_test():
    headers = get_cors_headers('DELETE')

    if request.method == 'OPTIONS':
        return make_response(('', 204, headers))

    return make_response(({'data': 'hey now, you DELETE-ed'}, 200, headers))
