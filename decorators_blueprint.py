"""
Run:
$ python3 decorators_blueprint.py

Tests:
$ curl -X GET http://localhost:8888/v1/test_decorator/
$ curl -X GET http://localhost:8888/v1/test_decorator/test1/randomvalue

"""
from functools import wraps

from flask import Blueprint
from flask import Flask
from flask import jsonify
from gevent.wsgi import WSGIServer


# Decorator
def tags(tag_key=None, tag_name=None):
    def tags_decorator(f):
        @wraps(f)
        def decorator_function(*args, **kwargs):
            print(args)
            print(kwargs)
            print(tag_key)
            print(tag_name)

            # extra value coming from url
            value = None
            if 'value' in kwargs:
                value = kwargs['value']

            data = {
                "data": {
                    "tag_key": tag_key,
                    "tag_name": tag_name,
                    "value": value
                }}
            kwargs.update(data)
            response = f(*args, **kwargs)
            return response

        return decorator_function

    return tags_decorator


# Defining endpoint
endpoints = Blueprint('test_decorator',
                      __name__,
                      url_prefix='/v1/test_decorator')


@endpoints.route('/', methods=['GET'])
@tags("color", "blue")
def test0(**kwargs):
    """
    Simple health check for now
    """
    data = kwargs.get('data', None)
    return jsonify(data), 200


@endpoints.route('/test1/<value>', methods=['GET'])
@tags("color", "blue")
def test1(value, **kwargs):
    """
    Simple health check for now
    """
    data = kwargs.get('data', None)
    return jsonify(data), 200


# Create Flask app
app = Flask(__name__)

# Register blueprints/endpoints
app.register_blueprint(endpoints)

if __name__ == '__main__':
    # start WSGI http server
    http_server = WSGIServer(
        ('', 8888),
        app
    )
    http_server.serve_forever()
