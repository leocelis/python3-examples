"""
Bug:
Name collision with param in update and in kwargs (decorator)

Fix: rename param in any
"""

from functools import wraps


# Decorator
def deco():
    def deco_decorator(f):
        @wraps(f)
        def decorator_function(*args, **kwargs):
            data = {'param': None}
            kwargs.update(data)

            try:
                response = f(*args, **kwargs)
            except Exception as err:
                print("Exception while sending updated kwargs {}".format(err))
                del kwargs['param']
                response = f(*args, **kwargs)

            return response

        return decorator_function

    return deco_decorator


# Endpoint with decorator
@deco()
def update(param, **kwargs):
    return param


update("random")
