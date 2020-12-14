from constraints.constraint1 import Constraint1

from constraints.constraint3 import Constraint3
from constraints.constraint4 import Constraint4
from constraints.constraint5 import Constraint5
from constraints.constraint6 import Constraint6
from constraints.constraint7 import Constraint7
from constraints.constraint8 import Constraint8
from constraints.cosntraint2 import Constraint2


class FileReader:
    def readDataFile(self, fileName):
        datas = []
        file1 = open(fileName, 'r')
        Lines = file1.readlines()
        for line in Lines:
            line = line.rstrip("\n")
            fields = line.split(',')
            datas.append(fields)
        return datas

    def readClueFile(self, fileName):
        constraintObjects = []
        file = open(fileName, 'r')
        lines = file.readlines()
        for line in lines:
            line = line.rstrip("\n")
            fields = line.split(' ')
            if fields[0] == "if": # for the ones start with if
                if len(fields) == 4: #if x=a then y=b
                    new_fields = fields[1].split('=')
                    x = new_fields[0]
                    a = new_fields[1]
                    new_fields2 = fields[3].split('=')
                    y = new_fields2[0]
                    b = new_fields2[1]
                    constraint = Constraint1(x, a, y, b)
                    constraintObjects.append(constraint)
                elif len(fields) == 5: #if x=a then not y=b
                    new_fields = fields[1].split('=')
                    x = new_fields[0]
                    a = new_fields[1]
                    new_fields2 = fields[4].split('=')
                    y = new_fields2[0]
                    b = new_fields2[1]
                    constraint = Constraint2(x, a, y, b)
                    constraintObjects.append(constraint)
                elif len(fields) == 7: #if x=a then either y=b or z=c
                    new_fields = fields[1].split('=')
                    x = new_fields[0]
                    a = new_fields[1]
                    new_fields2 = fields[4].split('=')
                    y = new_fields2[0]
                    b = new_fields2[1]
                    new_fields3 = fields[6].split('=')
                    z = new_fields3[0]
                    c = new_fields3[1]
                    constraint = Constraint3(x, a, y, b, z, c)
                    constraintObjects.append(constraint)

            else:
                if len(fields) < 6 and fields[0][0] != "{":
                    if fields[1] == "=":
                        new_fields = fields[0].split('(')
                        n = new_fields[0]
                        second_fields = new_fields[1].split("=")
                        x = second_fields[0]
                        a = second_fields[1].split(")")[0]
                        third_fields = fields[2].split("(")
                        fourth_fields = third_fields[1].split("=")
                        y = fourth_fields[0]
                        b = fourth_fields[1].split(")")[0]
                        if len(fields) == 5:
                            if fields[3] == "-":
                                m = fields[4]
                                constraint = Constraint4(x, a, y, b, n, (-1 * int(m)))  # n(x=a) = n(y=b) +m/-m
                                constraintObjects.append(constraint)
                            else:
                                m = fields[4]
                                constraint = Constraint4(x, a, y, b, n, int(m))  # n(x=a) = n(y=b) +m/-m
                                constraintObjects.append(constraint)
                        else:
                            constraint = Constraint4(x, a, y, b, n, 0)  # n(x=a) = n(y=b)
                            constraintObjects.append(constraint)
                    if fields[1] == ">": # n(x=a) > n(y=b)
                        new_fields = fields[0].split('(')
                        n = new_fields[0]
                        second_fields = new_fields[1].split("=")
                        x = second_fields[0]
                        a = second_fields[1].split(")")[0]
                        third_fields = fields[2].split("(")
                        fourth_fields = third_fields[1].split("=")
                        y = fourth_fields[0]
                        b = fourth_fields[1].split(")")[0]
                        constraint = Constraint5(x, a, y, b, n)
                        constraintObjects.append(constraint)
                    if fields[1] == "<": #n(x=a) < n(y=b)
                        new_fields = fields[0].split('(')
                        n = new_fields[0]
                        second_fields = new_fields[1].split("=")
                        x = second_fields[0]
                        a = second_fields[1].split(")")[0]
                        third_fields = fields[2].split("(")
                        fourth_fields = third_fields[1].split("=")
                        y = fourth_fields[0]
                        b = fourth_fields[1].split(")")[0]
                        constraint = Constraint6(x, a, y, b, n)
                        constraintObjects.append(constraint)
                else: #one of {x=a,y=b} corresponds to z=c other t=d
                    if len(fields) == 8:
                        first_field = fields[2]
                        first_field = first_field.replace("{", "")
                        first_field = first_field.replace("}", "")
                        second_field = first_field.split(",")
                        third_field = second_field[0].split("=")
                        x = third_field[0]
                        a = third_field[1]
                        fourth_field = second_field[1].split("=")
                        y = fourth_field[0]
                        b = fourth_field[1]
                        fifth_field = fields[5].split("=")
                        z = fifth_field[0]
                        c = fifth_field[1]
                        sixth_field = fields[7].split("=")
                        t = sixth_field[0]
                        d = sixth_field[1]
                        constraint = Constraint7(x, a, y, b, z, c, t, d)
                        constraintObjects.append(constraint)
                    else:   #{x=a,y=b,z=c} are all different
                        first_field = fields[0]
                        first_field = first_field.replace("{", "")
                        first_field = first_field.replace("}", "")
                        first_field = first_field.split(",")
                        second_field = first_field[0].split("=")
                        x = second_field[0]
                        a = second_field[1]
                        third_field = first_field[1].split("=")
                        y = third_field[0]
                        b = third_field[1]
                        fourth_field = first_field[2].split("=")
                        z = fourth_field[0]
                        c = fourth_field[1]
                        constraint = Constraint8(x, a, y, b, z, c)
                        constraintObjects.append(constraint)
        return constraintObjects