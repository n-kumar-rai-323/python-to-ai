def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, *kwargs)
    return wrapper

from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Running")
        return func(*args, **kwargs)
    return wrapper