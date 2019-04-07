print_hello = True
if print_hello:
	print('hello python!')


# if else statements
# if in
known_people = ['John', 'Anna', 'Mary']
person = input('Enter the person you know: ')

if person in known_people:
	print('You know {}!'.format(person))
else:
	print('You dunno know {}!'.format(person))


def who_do_you_know():
	people = input('Enter the names of people you know, seperated by commas: ')
	people_list = people.split(',')

	people_list_without_spaces = []
	for person in people_list:
		people_list_without_spaces.append(person.strip())

	return people_list_without_spaces


def ask_user():
	person = input('Enter a name of someone you know: ')
	if person in who_do_you_know():
		print('You know {}!'.format(person))


ask_user()