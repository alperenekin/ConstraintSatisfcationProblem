class Constraint7:  # one of {x=a,y=b} corresponds to z=c other t=d

    def __init__(self, x, a, y, b, z, c, t, d):
        self.x = x
        self.a = a
        self.y = y
        self.b = b
        self.z = z
        self.c = c
        self.t = t
        self.d = d

    def constraintFunction(self, domains, index):
        domainOfZforX = []
        domainOfZforY = []
        domainOfTforX = []
        domainOfTforY = []
        for i in range(len(domains)):
            domainOfX = domains[i][self.x]
            domainOfY = domains[i][self.y]

            if self.a in domainOfX and len(domainOfX) == 1:
                domainOfZforX = domains[i][self.z]
                domainOfTforX = domains[i][self.t]

            if self.b in domainOfY and len(domainOfY) == 1:
                domainOfZforY = domains[i][self.z]
                domainOfTforY = domains[i][self.t]

        if len(domainOfZforX) == 1 and len(domainOfZforY) == 1 and len(domainOfTforX) == 1 and len(domainOfTforY) == 1:
            if domainOfZforX[0] != self.c and domainOfZforY[0] != self.c:
                return False
            if domainOfTforX[0] != self.d and domainOfTforY[0] != self.d:
                return False
            if domainOfTforX[0] == self.d and domainOfZforX[0] == self.c:
                return False
            if domainOfTforY[0] == self.d and domainOfZforY[0] == self.c:
                return False

        return True
