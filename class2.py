class Student:

    shool_name = 'ABC School '

    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Harry", 12)

print('Student Name:', s1.name, s1.age)
print('School Name:', Student.shool_name)

s2 = Student("Jessa", 12)
print('Student Name:', s2.name, s2.age)
print('School Name:', Student.shool_name)
