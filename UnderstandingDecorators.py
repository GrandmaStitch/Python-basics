# http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/

# 1.Functions
print('--Functions:')
def foo1():
    return 1

print(foo1())

# 2.Scope
print('--Scope:')
a_string = "This is a global variable"
def foo2():
    print(locals())

print(globals())

foo2()

# 3.variables resolution rules
print('--variables resolution rules:')
def foo3():
    print(a_string)

# Python looks for a local variable in our function and not finding one, looks for a global variable of the same name.
foo3()

a_string = "This is a global variable"
def foo4():
    a_string = 'test'
    print(locals())

foo4()
print(a_string)

# 4.Variable liftime
print('--Variable liftime:')
def foo5():
    x = 1

print(foo5())
try:
    print(x)
except NameError as e:
    print(e)

# 5.Function arguments and parameters
print('--Function arguments and parameters:')
def foo6(x):
    print(locals())

foo6(1)

def foo7(x, y=0):
    print(x-y)

# function parameters can have names or positions
foo7(3,2)
try:
    foo7()
except TypeError as e:
    print(e)
# we can use named arguments to functions defined only with positional parameters and vice-versa!
foo7(y=2, x=3)

# 6.Nested functions
print('--Nested functions:')
def outer():
    x = 1
    def inner():
        print(x)
    inner()

outer()

# 7.Functions are first class objects in Python
print('--Functions are first class objects in Python:')
print(issubclass(int, object))

def foo8():
    pass

print(foo8.__class__)
# classes are objects in Python
print(issubclass(foo8.__class__, object))

def add(x, y):
    return x+y

def sub(x, y):
    return x-y

def apply(func, x, y):
    return(func(x, y))

# functions are just regular values like any other kind of value in Python. That means you can pass functions to functions as arguments or return functions from functions as return values!
print(apply(add, 3, 2))
print(apply(sub, 3, 2))

def outer1():
    def inner1():
        print('Inside inner1')
        return 'This is inner1 return'
    return inner1 # 1

foo = outer1()
print(foo.__class__)
print(f'foo is an object: {issubclass(foo.__class__, object)}')
# function calls
# because #1 here will call inner1, so we can call outer1(). It is a functon
print(foo())
print(outer1()())

# 8.Closures
# Python supports a feature called function closures which means that inner functions defined in non-global scope remember what their enclosing namespaces looked like at definition time.
print('--Closures:')
def outer2():
    x = 1
    def inner2():
        print(x)
    return inner2

foo = outer2()
print(foo.__closure__)

# the function inner is being newly defined each time the function outer is called.
def outer3(x):
    def inner3():
        print(x)
    return inner3

outer3(1)()
outer3(2)()

# 9.Decorators!
# A decorator is just a callable that takes a function as an argument and returns a replacement function.
print('--Decorators:')
# We defined a function named outer4 that has a single parameter some_func. Inside outer4 we define an nested function named inner4. The inner4 function will print a string then call some_func, catching its return value at point #1. The value of some_func might be different each time outer4 is called, but whatever function it is we’ll call it. Finally inner4 returns the return value of some_func() + 1 - and we can see that when we call our returned function stored in decorated at point #2 we get the results of the print and also a return value of 2 instead of the original return value 1 we would expect to get by calling foo.
# We could say that the variable decorated is a decorated version of foo - it’s foo plus something. In fact if we wrote a useful decorator we might want to replace foo with the decorated version altogether so we always got our "plus something" version of foo.
def outer4(some_func):
    def inner4():
        print('before some_func')
        ret = some_func() # 1
        return ret + 1
    return inner4

def foo9():
    return 1

decorated = outer4(foo9) # 2

print(decorated())

def inner5():
        print('It\'s a function.')

# inner5 is a function
print(f'inner5 is {type(inner5)}')
# inner5 is a function call
print(f'inner5() is  {type(inner5())}')

# The @ symbol applies a decorator to a function
# Again - using decorators is easy! Even if writing useful decorators like staticmethod or classmethod would be difficult, using them is just a matter of prepending your function with @decoratorname!
print('--The @ symbol applies a decorator to a function:')
@outer4
def foo9():
    return 1

print(foo9())

# 11.*args and **kwargs
print('--*args and **kwargs:')
# Let’s write a decorator that increments a counter for every function call of every decorated function without changing any of it’s decorated functions. This means it would have to accept the calling signature of any of the functions that it decorates and also call the functions it decorates passing on whatever arguments were passed to it.
def one(*args):
    print(args)

one()
one(1,2,3)

def two(x, y, *args):
    print(x, y, args)

two('a','b','c', 'd')

# The * operator can also be used when calling functions and here it means the analogous thing.
def add(x, y):
    return x+y

lst = [1,2]

print(add(lst[0], lst[1]))
print(add(*lst))

# Things get only slightly more complicated when we introduce ** which does for dictionaries & key/value pairs exactly what * does for iterables and positional parameters.
def foo10(**kwargs):
    print(kwargs)

foo10()
foo10(x=1, y=2)

dct = {'x':1, 'y':2}
def bar(x,y):
    return x+y

print(bar(**dct))

# 12.More generic decorators
print('--More generic decorators:')
def logger(func):
    def inner(*args, **kwargs):
        print('Arguments were: %s, %s' % (args, kwargs))
        return func(*args, **kwargs)
    return inner

@logger
def fool1(x, y):
    return x*y

fool1(3,4)
print(fool1(3,4))

@logger
def fool2():
    return 2
print(fool2())



