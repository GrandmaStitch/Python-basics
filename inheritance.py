# super() method
# origin object

class student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    # all subclass will inherit this classmethod
    @classmethod
    # origin object
    def friend(cls, origin, friend_name, *args):
        return cls(friend_name, origin.school, *args)


class working_student(student):
    def __init__(self, name, school, salary, position):
        # super() method
        # we use this method to inherit the parent class student's properties, here is name and school
        # here the super() method will call the __init__() method from the parent class
        super().__init__(name, school)
        self.salary = salary
        self.position = position


anna = working_student('Anna', 'MIT', 20.00, 'Software Engineer')
print(anna)
print(anna.name)
print(anna.school)
print(anna.salary)
print(anna.position)

john = working_student.friend(anna, 'John', 30.00, 'Software Engineer')
print(john)
print(john.name)
print(john.school)
print(john.salary)
print(john.position)
