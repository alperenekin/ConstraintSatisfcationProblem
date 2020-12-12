class Constraint5:  #  n(x=a) > n(y=b)

    def __init__(self, x, a, y, b, n, m):
        self.x = x
        self.a = a
        self.y = y
        self.b = b
        self.n = n
        self.m = m

    def constraintFunction(self, dictionary):
        if self.a in dictionary[self.x] : #== yap
            for i in range(len(dictionary[self.y]) - 1, -1, -1):
            # for value in dictionary[self.y]:
                if dictionary[self.y][i] == self.b:
                     del dictionary[self.y][i]

