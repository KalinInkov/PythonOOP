class Person:
    fname  = "Gosho"

    def __init__(self,first_name, last_name,age):
        self.grades = []
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def add_grade(self, subject, grade):
           self.grades.append((subject,grade))
    def print_grades(self):
        print(self.grades)

    def __new__(self, *args, **kwargs):
        return 'Empty Person'


pesho = Person('Guzi', 'Guzev',19)

print(pesho)
print(pesho.first_name)
print(pesho.fname)

'''
__call__
__new__
__init__
'''