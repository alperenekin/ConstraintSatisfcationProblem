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
        firstOption = domains[domainIndex][self.x] #get values for x in index we are in
        secondOption = domains[domainIndex][self.y] #get values for y in index we are in
        thirdOption = domains[domainIndex][self.z] #get values for z in index we are in

        if len(firstOption) == 1 and self.a == firstOption[0]: # "a" should be selected
            if self.b not in secondOption and self.c not in thirdOption:
                return False

            if len(secondOption) == 1 and len(thirdOption) == 1: # "a" 
                if self.b == secondOption[0] and self.c == thirdOption[0]:
                    return False

        return True
