class Constraint1:  # agac yapisi icinde bir dugum
    def __init__(self, x, a, y, b):
        self.x = x
        self.a = a
        self.y = y
        self.b = b

    def constraintFunction(self, dictionary):
        if self.a in dictionary[self.x]:  # == yap
            indexOfa = dictionary[self.x].index(self.a)
            if (self.b == dictionary[self.y][indexOfa]):
                print("true")
