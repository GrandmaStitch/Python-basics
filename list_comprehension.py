my_list = [0, 1, 2, 3, 4]
an_equal_list = [x for x in range(5)]
print(an_equal_list)


multiply_list = [x * 3 for x in range(5)]
print(multiply_list)


# % modulo
print(8 % 3)


# get even numbers
print([n for n in range(10) if n % 2 == 0])


# .strip() method, .lower() method
people_you_know = ['Rolf', 'John', 'anna', 'GREG']
people_list = [person.strip().lower() for person in people_you_know]
print(people_list)


print()
def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1

print(my_range(5))