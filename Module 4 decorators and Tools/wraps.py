# def logger(func):
#     def wrapper():
#         print("Running...")
#         func()

#     return wrapper


# @logger
# def hello():
#     print("Hello")


# hello()

# print(hello.__name__)

from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper():
        print("Running...")
        func()

    return wrapper


@logger
def hello():
    """This is hello"""
    print("Hello")

print(hello.__doc__)
print(hello.__name__)