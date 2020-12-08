class FileReader:
    datas =[]
    def readDataFile(self,fileName):
        file1 = open(fileName, 'r')
        Lines = file1.readlines()
        for line in Lines:
            fields = line.split(',')
            FileReader.datas.append(fields)

if __name__ == '__main__':
    fileReader = FileReader()
    fileReader.readDataFile("data-1.txt")
    print(fileReader.datas)