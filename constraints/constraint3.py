class Constraint3:  # if x=a then either y=b or z=c
    def __init__(self, x, a, y, b,z,c):
        self.x = x
        self.a = a
        self.y = y
        self.b = b
        self.z = z
        self.c = c

    def constraintFunction(self, dictionary):
        if self.a in dictionary[self.x] : #== yap
            for i in range(len(dictionary[self.y]) - 1, -1, -1):
            # for value in dictionary[self.y]:
                if dictionary[self.y][i] == self.b:
                     del dictionary[self.y][i]

