from constraints.base_constraint import BaseConstraint


class Constraint1(BaseConstraint):
    def __init__(self, x, a, y, b):
        self.x = x
        self.a = a
        self.y = y
        self.b = b

    def constraintFunction(self, domains, domainIndex):
        firstOption = domains[domainIndex][self.x]
        secondOption = domains[domainIndex][self.y]

        if len(firstOption) == 1 and self.a == firstOption[0]: # check if "a" selected
            if self.b not in secondOption:
                return False
        else:
            if len(secondOption) == 1 and self.b == secondOption[0]: # check if "b" selected
                if self.a not in firstOption:
                    return False
        return True
