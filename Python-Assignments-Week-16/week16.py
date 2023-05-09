
def hello(f):
    def welcome():
        print("Welcome From Welcome Function")
    welcome()
    f()

    def letsGo():
        print("Let's Go From Let's Go Function")
    letsGo()


@hello
def decorator():
    print("This is From decorator Function")
