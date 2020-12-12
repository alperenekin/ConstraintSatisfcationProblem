from constraints.base_constraint import BaseConstraint


class Constraint4(BaseConstraint):  #  n(x=a) = n(y=b) + m

    def __init__(self, x, a, y, b, n, m):
        self.x = x
        self.a = a
        self.y = y
        self.b = b
        self.n = n
        self.m = m

    def constraintFunction(self, domains):
        for i in range(len(domains)):
            if self.a in domains[i][self.x]:



        if (len(firstOption) == 1 and self.a == firstOption[0]):  # TODO try if self.b ==firstOption[0] this only enough
            if (self.b not in secondOption and self.c not in thirdOption):
                print("false")
                return False

        print("true")
        return True

