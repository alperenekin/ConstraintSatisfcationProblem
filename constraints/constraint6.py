class Constraint6:  #  n(x=a) < n(y=b)

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
                if len(domainOfX) == 1 and self.a in domainOfX:
                    year = domains[i][self.n] #find year of a
                    if len(year) == 1:
                        for j in range(len(domains)):
                            domainOfY = domains[j][self.y]
                            if self.b in domainOfY:
                                if i != j:
                                    second_year = domains[j][self.n] #find year of b
                                    for second in second_year:
                                        if int(year[0]) >= int(second):  # if year of first not greater than second then it is false
                                            return False
        return True

