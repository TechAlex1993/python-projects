class Person:
    def __init__(self, name, sex, profession):
        self.name = name
        self.sex = sex
        self.profession = profession

    def show(self):
        print('Name:', self.name, 'Sex:', self.sex, 'Profession:', self.profession)

    def work(self):
        print(self.name, 'working as a', self.profession)

jessa = Person('Jessa', 'Female', 'Software Engineer')
jessa.show()
jessa.work()

print('Name:', jessa.name)
print('Sex:', jessa.sex)
print('Profession:', jessa.profession)