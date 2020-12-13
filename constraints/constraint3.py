from constraints.base_constraint import BaseConstraint


class Constraint3(BaseConstraint):  # if x=a then either y=b or z=c
    def __init__(self, x, a, y, b, z, c):
        self.x = x
        self.a = a
        self.y = y
        self.b = b
        self.z = z
        self.c = c

    def constraintFunction(self, domains, domainIndex):
        firstOption = domains[domainIndex][self.x]
        secondOption = domains[domainIndex][self.y]
        thirdOption = domains[domainIndex][self.z]

        if len(firstOption) == 1 and self.a == firstOption[0]:
            if self.b not in secondOption and self.c not in thirdOption:
                print("constraint 3 false")
                return False

            if len(secondOption) == 1 and len(thirdOption) == 1:
                if self.b == secondOption[0] and self.c == thirdOption[0]:
                    print("constraint 3 false")
                    return False


        print("constraint 3 true")
        return True
