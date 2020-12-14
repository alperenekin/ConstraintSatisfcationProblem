from constraints.base_constraint import BaseConstraint


class Constraint2(BaseConstraint):  # if x=a then not y=b
    def __init__(self, x, a, y, b):
        self.x = x
        self.a = a
        self.y = y
        self.b = b

    def constraintFunction(self, domains, domainIndex):
        firstOption = domains[domainIndex][self.x] #get the values for x
        secondOption = domains[domainIndex][self.y] #get the values for y

        if len(firstOption) == 1 and self.a == firstOption[0]: #if "a" is selected and "b" is selected
            if (len(secondOption)) == 1 and self.b == secondOption[0]:
                return False
        return True

