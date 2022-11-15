def check_login(f):
    def wrapper():
        print("Checking if user is loged in...")
        f()
        print("User is logged in")
    return wrapper
    
@check_login
def signin():
    print("Please log me in!")

signin() 