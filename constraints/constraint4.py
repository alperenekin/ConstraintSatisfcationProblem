from constraints.base_constraint import BaseConstraint


class Constraint4(BaseConstraint):  #  n(x=a) = n(y=b) + m

    def __init__(self, x, a, y, b, n, m):
        self.x = x
        self.a = a
        self.y = y
        self.b = b
        self.n = n
        self.m = m

    def constraintFunction(self, domains,index):
        for i in range(len(domains)):
            domainOfX = domains[i][self.x]
            if self.a in domainOfX:
                if len(domainOfX) == 1 and  self.a in domainOfX:
                    year = domains[i][self.n]
                    if len(year) == 1:
                        for j in range(len(domains)):
                            domainOfY = domains[j][self.y]
                            if self.b in domainOfY and len(domainOfY) == 1:
                                second_year = domains[j][self.n]
                                if year[0] == second_year[0]: # can not belong to same subject
                                    return False
                                else:
                                    for second in second_year:
                                        if int(year[0]) != int(second) + int(self.m):  # if year of first not greater than second then it is false
                                            print("cosntraint 4 false")
                                            return False
        print("cosntraint 4 true")
        return True

