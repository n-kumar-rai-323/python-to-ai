def logger(func):
    def wrapper():
        print("Calling Function")
        func()
        print("Completed")
    return wrapper
@logger
def save_user():
    print("Saving User")
save_user()


