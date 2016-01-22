# This is our decorator
def simple_decorator(f):
    # This is the new function we're going to return
    # This function will be used in place of our original definition
    def wrapper():
        print "Entering Function"
        f()
        print "Exited Function"

    return wrapper

@simple_decorator 
def hello():
    print "Hello World"

hello()


def decorator_factory(enter_message, exit_message):
    # We're going to return this decorator
    def simple_decorator(f):
        def wrapper():
            print enter_message
            f()
            print exit_message

        return wrapper

    return simple_decorator

@decorator_factory("Start", "End")
def hello():
    print "Hello World"

hello()