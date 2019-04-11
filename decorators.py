import functools

# decorator without arguments
def my_decorator(func):
    # this method allows us to wrap a function we pass in as a parameter
    @functools.wraps(func)
    def function_that_runs_func():
        print('In the decorator!')
        func()
        print('After the decorator!')
    # we should return the function for the decorator to use
    return function_that_runs_func

# a decorator is just a function that gets call before another function
# in this case, when we use the decorator, we pass my_function() as a parameter in my_decorator()
@my_decorator
def my_function():
    print('I\'m the function!')

# my_function()


# decorator with arguments
def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print('In the decorator!')
            if number == 48:
                print('Don\'t run the function')
            else:
                func(*args, **kwargs)
            print('After the decorator!')
        return function_that_runs_func
    return my_decorator

@decorator_with_arguments(49)
def my_function_too(x, y):
    print(x + y)

@decorator_with_arguments(48)
def my_function_tooo():
    print('hello')

my_function_too(1, 2)
my_function_tooo()

