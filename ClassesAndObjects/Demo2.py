class Fraction:
    def __init__(self,nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator
    def __add__(self, other):
        nominator = self.nominator*other.denominator+\
            other.nominator+self.denominator
        denominator = self.denominator*other.denominator
        return Fraction(nominator,denominator)
    def __str__(self):
        return f'{self.nominator}/{self.denominator}'
f1 = Fraction(1,2)
f2 = Fraction(3,4)
print(f1+f2)
print(Fraction(1,2)==Fraction(1,2))

print(f1.__dict__)
