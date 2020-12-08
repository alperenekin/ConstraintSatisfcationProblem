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
                    print("first rule")
                elif(len(fields) == 5):
                    print("second rule")
                elif(len(fields) == 7):
                 print("third rule")
            else:
                if(len(fields) < 6):
                    print("n(x=a) falan filan")
                else:
                    print("son")


if __name__ == '__main__':
    fileReader = FileReader()
    fileReader.readDataFile("data-1.txt")
    fileReader.readClueFile("clues-1.txt")