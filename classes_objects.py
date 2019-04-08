# a class is a blueprint

lottery_player_dict = {
	'name': 'Rolf',
	'numbers': (5, 9, 12, 3, 1, 21)
}


class lottery_player:
	# define the object itself
	# this is the unique method every object should have
	# instancemethod
    def __init__(self):
        self.name = 'Rolf' # object properties
        self.numbers = (5, 9, 12, 3, 1, 21) # object properties

    # define a method
    def total(self):
    	return sum(self.numbers)

player = lottery_player()

print(player) # the object
print(player.name) # the object property
print(player.numbers) # the object property
print(player.total())

# create two objects
# both of the two objects have the same properties and methods 
player_one = lottery_player()
# change the object player_one's numbers property
player_one.numbers = (1, 2, 3, 4, 5, 6)
player_two = lottery_player()

print(player_one == player_two)
print(player_one.name == player_two.name)
print(player_one.numbers == player_two.numbers)


class student:
	
    def __init__(self, name, school):
    	self.name = name
    	self.school = school
    	self.marks = []
    
    # define the averge method to calculate the averge of marks
    def averge(self):
    	return sum(self.marks) / len(self.marks)

anna = student('Anna', 'MIT')
anna.marks.append(56)
anna.marks.append(71)
print(anna.marks)
print(anna.averge())
print(student)

# @classmethod
# @staticmethod


class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    def from_strings(self, date_as_string):
    	day, month, year = (self.day, self.month, self.year)
    	day, month, year = map(int, date_as_string.split('-'))
    	return day, month, year

    @classmethod
    # cls is an object that holds the class itself, not an instance of the class.
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999

date2 = Date.from_string('11-09-2012')
is_date = Date.is_date_valid('11-09-2012')

print('date2: {}'.format(date2))
print(date2.year)
print(Date.from_strings('11-09-2012'))
print('is_date: {}'.format(is_date))

https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner

