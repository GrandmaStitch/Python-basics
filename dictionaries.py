# a dictionary is a key value set
my_dict = {'name': 'Lucky', 'age': 6, 'hobbies': ['walks', 'eating', 'sleeping', 'play']}


lottery_player = {
	'name': 'Rolf',
	'numbers': (13, 45, 66, 23, 22)
}

print(sum(lottery_player['numbers']))

lottery_player['name'] = 'John'
print(lottery_player)

print(lottery_player.items)
print(lottery_player.items())
print(lottery_player.keys())
print(lottery_player.values())


student_list = [
    {
        'name': 'Jose',
        'school': 'Computing',
        'grades': (1, 2, 3)
    },
    {
        'name': 'Amy',
        'school': 'Computing',
        'grades': (0, 0, 0)
    },
    {
        'name': 'Rolf',
        'school': 'Computing',
        'grades': (2, 10, 55)
    }
]

def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total += sum(student['grades'])
        count += len(student['grades'])
    return int(total / count)

print(average_grade_all_students(student_list))

