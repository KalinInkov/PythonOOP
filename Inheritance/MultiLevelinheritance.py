class Person:
    def __init__(self, name):
        self.name = name


class SoftwareDeveloper(Person):
    def __init__(self, name, tech_stack):
        super().__init__(name)
        self.tech_stack = tech_stack


class TechnicalLead(SoftwareDeveloper):
    def __init__(self,name,tech_stack, team_size):
        super().__init__(name,tech_stack)
        self.team_size = team_size



t1 = TechnicalLead("Guzi",['python','React'],15)
print(t1.name)
print(t1.tech_stack)

print(isinstance(t1,TechnicalLead))




