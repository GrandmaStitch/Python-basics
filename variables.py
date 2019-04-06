# A variable is a box for a value, which can be of various types

# Data types
# integer
num1 = 1
num2 = 2

# string
var1 = 'hello'
var2 = 'world'
any_variable_name = 'hello world'

# float
x = 1.0
y = 1.55

# boolean
true_boolean = True
false_boolean = False


# Basic math
total1 = num1 + num2
total2 = num1 - num2
total3 = num1 * num2
total4 = num1 / num2
total5 = num1 % num2


# Casting
a = str(num1)
b = int(x)
c = float(num1)
print(f'{a}: {type(a)}')
print(f'{b}: {type(b)}')
print(f'{c}: {type(c)}')

##############

# list
my_list = [1, 2, 3, 1, 4, 5, 6]

# tuple(immutable)
my_tuple = (1, 2, 3, 4, 5, 6)

# set(unique & unordered)
my_set = {1, 3, 2, 3, 5, 4}


# list methods and operations
# .append() method
my_list.append(100)
print(my_list)

# .remove() method
my_list.remove(100)
print(my_list)

# list
my_list += [100]
print(my_list)

# list index
print(my_list[0])

# tuple
my_tuple += (100,)
print(my_tuple)

try:
	my_tuple[0] = 100
except:
	print('tuple is immutable!')

# set
print(f'set is unique: {my_set}')

try:
	my_set[0] = 100
except:
	print('set is unordered!')

my_set.add(6)
print(my_set)

your_lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9, 11}

# .intersection() method
print(your_lottery_numbers.intersection(winning_numbers))
# .union() method
print(your_lottery_numbers.union(winning_numbers))
# .difference() method
print(your_lottery_numbers.difference(winning_numbers))





