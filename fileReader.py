from constraints.constraint1 import Constraint1
class FileReader:
    def readDataFile(self,fileName):
        datas = []
        file1 = open(fileName, 'r')
        Lines = file1.readlines()
        for line in Lines:
            fields = line.split(',')
            datas.append(fields)
        return datas

    def readClueFile(self,fileName):
        constraintObjects = []
        file = open(fileName, 'r')
        lines = file.readlines()
        for line in lines:
            fields = line.split(' ')
            if(fields[0] == "if"):
                if(len(fields) == 4):
                    new_fields = fields[1].split('=')
                    x = new_fields[0]
                    a = new_fields[1]
                    new_fields2 = fields[3].split('=')
                    y = new_fields2[0]
                    b = new_fields2[1]
                    constraint = Constraint1(x,a,y,b)
                    constraint.constraintFunction()
                    constraint.getB()
                    constraintObjects.append(constraint)
                elif(len(fields) == 5):
                    print("second rule")
                elif(len(fields) == 7):
                 print("third rule")
            else:
                if(len(fields) < 6):
                    print("n(x=a) falan filan")
                else:
                    print("son")
        return constraintObjects

if __name__ == '__main__':
    fileReader = FileReader()
    fileReader.readDataFile("data-1.txt")
    array = fileReader.readClueFile("clues-1.txt")
    print(array)
