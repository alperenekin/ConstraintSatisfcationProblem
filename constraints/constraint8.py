class Constraint8:  #  {x=a,y=b,z=c} are all different
#{boats=AlphaOne,sailors=VickyEstes,sailors=TaraCarroll} are all different

    def __init__(self, x, a, y, b, z, c):
        self.x = x
        self.a = a
        self.y = y
        self.b = b
        self.z = z
        self.c = c

    def constraintFunction(self, domains,index):
        for subject in domains:
            if self.a in subject[self.x] and len(subject[self.x]) == 1:
                if self.b in subject[self.y] and len(subject[self.y]) == 1:
                    return False
                if self.c in subject[self.z] and len(subject[self.z]) == 1:
                    return False

            if self.b in subject[self.y] and len(subject[self.y]) == 1:
                if self.c in subject[self.z] and len(subject[self.z]) == 1:
                    return False
        return True






