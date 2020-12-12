from constraints.constraint1 import Constraint1
import copy


class FileReader:
    def readDataFile(self, fileName):
        datas = []
        file1 = open(fileName, 'r')
        Lines = file1.readlines()
        for line in Lines:
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
            if (fields[0] == "if"):
                if (len(fields) == 4):
                    new_fields = fields[1].split('=')
                    x = new_fields[0]
                    a = new_fields[1]
                    new_fields2 = fields[3].split('=')
                    y = new_fields2[0]
                    b = new_fields2[1]
                    constraint = Constraint1(x, a, y, b)
                    #constraint.constraintFunction(dict)
                    constraintObjects.append(constraint)
                elif (len(fields) == 5):
                    print("second rule")
                elif (len(fields) == 7):
                    print("third rule")
            else:
                if (len(fields) < 6):
                    if (fields[1] == "="):
                        print("rule4 , rule 5, rule6")
                    if (fields[1] == ">"):
                        print("rule 7")
                    if (fields[1] == "<"):
                        print("rule 8")
                else:
                    print("rule 9 -10")
        return constraintObjects


if __name__ == '__main__':
    fileReader = FileReader()
    data1 = fileReader.readDataFile("data-1.txt")
    domains = []
    for i in range(4):
        copyData1 = copy.deepcopy(data1)
        dict = {
            copyData1[0][0]: copyData1[0][1:],
            copyData1[1][0]: copyData1[1][1:],
            copyData1[2][0]: copyData1[2][1:],
            copyData1[3][0]: copyData1[3][1:],
        }
        domains.append(dict)

    answer = {
        data1[0][0]: ["2006", "", "", ""],
        data1[1][0]: ["", "", "", ""],
        data1[2][0]: ["greatDane", "", "", ""],
        data1[3][0]: ["", "", "", ""]
    }
    print(dict)
    array = fileReader.readClueFile("clues-1.txt", answer)
