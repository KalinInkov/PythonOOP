import math


class Circle:
    #class attribute, class variable
    pi=math.pi

    def __init__(self, raduis):
        #object attribute, instance attribute, intance variable
        self.raduis = raduis
    def calc_rad(self):
        return self.raduis*self.raduis*self.pi

print(Circle(10).calc_rad())
