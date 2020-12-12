class Constraint2:  # if x=a then not y=b
    def __init__(self, x, a, y, b):
        self.x = x
        self.a = a
        self.y = y
        self.b = b

    def constraintFunction(self, dictionary):
        if self.a in dictionary[self.x] : #== yap
            for i in range(len(dictionary[self.y]) - 1, -1, -1):
            # for value in dictionary[self.y]:
                if dictionary[self.y][i] == self.b:
                     del dictionary[self.y][i]

