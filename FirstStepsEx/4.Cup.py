class Cup:
    def __init__(self, size: int, start_quantity: int):

        self.size = size
        self.start_quantity = start_quantity


    def fill(self, quantity):
        if self.size >= quantity + self.start_quantity:
            self.size -= quantity + self.start_quantity
        return self.size

    def status(self):
        return self.size


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)

