def greet(func):

    def myfunc():
        print("Good Morning")

        func()
        print("Thanks for using this function")
    return myfunc

@greet
def hello():
    print("Hello world!")

hello ()

