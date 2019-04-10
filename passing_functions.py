# lambda function
def methodception(another):
    return another()

def add_two_numbers():
    return 35 + 77

def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3))
# no need to pass parameters when the methodceptions call another methods
# in this case, methodception method is helpful
print(methodception(add_two_numbers))
# in this case, methodception method is useless
print(methodception(add_numbers))
# lambda function is an anonymous function
# lambda function is always in one line
print(methodception(lambda: 35 + 77))


my_list = [13, 22, 34, 55, 67, 100]
print(list(filter(lambda x: x != 13, my_list)))

# this one is identically the same as the last one
def not_thirteen(x):
    return x != 13
    return list
print(list(filter(not_thirteen, my_list)))





