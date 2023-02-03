class SchoolMember:
    """Represents any school Member"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Initialized {}".format(self.name))

    def tell(self):
        """Tell My Details"""
        print("Name:{} Age: {}".format(self.name, self.age), end="\n")

class Teacher(SchoolMember):
    """Class to represent a Teacher"""
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary 
        print('Initialized Teacher: {}'.format(self.name))
        
    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}'.format(self.salary))


class Student(SchoolMember):
    """Class to represent a Student"""
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print("Initialized Student: {}".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks "{:d}"'.format(self.marks))

t = Teacher("Mr.Ochieng", 40, 30000)
s = Student("Baby Panda", 12, 95)

#print a blank line
print()

members = [t,s]
for member in members:
    member.tell()
