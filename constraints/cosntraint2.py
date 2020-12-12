from constraints.base_constraint import BaseConstraint


class Constraint2(BaseConstraint):  # if x=a then not y=b
    def __init__(self, x, a, y, b):
        self.x = x
        self.a = a
        self.y = y
        self.b = b

    def constraintFunction(self, domains, domainIndex):
        firstOption = domains[domainIndex][self.x]
        secondOption = domains[domainIndex][self.y]

        if len(firstOption) == 1 and self.a == firstOption[0]:  # TODO try if self.b ==firstOption[0] this only enough
            if (len(secondOption)) == 1 and self.b == secondOption[0]:
                print("false")
                return False

        print("true")
        return True

