# 21. Implement a decorator @login_required that checks if a user is logged 
# in before executing a function.

def login_required(func):
    def wrapper():
        logged_in = True
        if logged_in:
            func()
        else:
            print("Please log in to continue.")
    return wrapper

@login_required
def dashboard():
    print("Welcome to your dashboard!")

dashboard()
