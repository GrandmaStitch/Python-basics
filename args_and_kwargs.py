def multiple_arguments_method(arg1, arg2, arg3):
    print(arg1 + arg2 + arg3)

multiple_arguments_method(1, 2, 3)


# *args let's us use muptiple arguments
def what_are_args(*args):
    print(args)

what_are_args(1, 2, 3, 4, 5, 6, 7)
what_are_args('hello', 'python', '*args')


# kyargs = keyword arguments
def what_are_kwargs(**kwargs):
    print(kwargs)

what_are_kwargs(args1='h', args2='e', args3='l', args4='l', args5='o')

def args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

# *args returns a tuple
args_kwargs(1, 2, 3)
args_kwargs(1, 2, 3, 'hello', 'python')
# **kwargs returns a dictionary
args_kwargs(1, 2, 3, name='Kelly', location='LA')
