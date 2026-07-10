def my_decorator(func):
    def wrapper():
        print("Before Function")
        func()
        print("After Function")
    return wrapper
@my_decorator
def hello():
    print("Hello")
    
hello()
