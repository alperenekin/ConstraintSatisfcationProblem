class Constraint1:  # agac yapisi icinde bir dugum
    def __init__(self, x, a, y, b):
        self.x = x
        self.a = a
        self.y = y
        self.b = b

    def constraintFunction(self):
        if self.x == self.x:
            self.y = self.b

    def getB(self):
        print(self.y)
