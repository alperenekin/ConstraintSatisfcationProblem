import copy
import sys

from fileReader import FileReader

if __name__ == '__main__':
    class Node:  # agac yapisi icinde bir dugum
        def __init__(self, domain):
            self.domain = domain

        def setDomain(self, domain):
            self.domain = domain

        def getDomains(self):
            return self.domains


    class CSPSolution:
        file1 = ""
        file2 = ""

        def __init__(self, optionNumber):
            fileReader = FileReader()
            self.chooseFile(optionNumber)
            data1 = fileReader.readDataFile(self.file1)
            self.constraints = fileReader.readClueFile(self.file2)

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

            self.rootNode = Node(domains)

        def chooseFile(self, optionNumber):
            if optionNumber == "1":
                self.file1 = "data-1.txt"
                self.file2 = "clues-1.txt"
            elif optionNumber == "2":
                self.file1 = "data-2.txt"
                self.file2 = "clues-2.txt"
            elif optionNumber == "3":
                self.file1 = "data-3.txt"
                self.file2 = "clues-3.txt"

        def isAllDomainsHaveOneElement(self, node):
            for dictionaryDomain in node.domain:
                for subject in dictionaryDomain:
                    if len(dictionaryDomain[subject]) != 1:
                        return False
            return True

        def isSolved(self, node):
            if self.isAllDomainsHaveOneElement(node) and self.checkConstraints(
                    node.domain):  # to check if answer passes from constraints
                self.printResult(node.domain)
                sys.exit()
                return node.domain

        def solveCSP(self):
            return self._solve(self.rootNode)

        def _solve(self, node):
            domainCount = 0
            elementCount = 0
            self.isSolved(node)
            for dictionaryDomain in node.domain:  # for every domains
                for subject in dictionaryDomain:
                    if len(dictionaryDomain[subject]) > 1:  # if there is only one element then i can check next one
                        for values in dictionaryDomain[subject]:  # check all elements in domaint
                            elementCount += 1
                            if self.checkConstraints(node.domain):  # if this checking is valid
                                newDomain = copy.deepcopy(node.domain)
                                newNode = Node(newDomain)
                                self.restrictDomain(newNode.domain, values, subject, domainCount)
                                self._solve(newNode)
                            if len(dictionaryDomain[
                                       subject]) == elementCount:  # if i checked all elements in domain, i will backtrack
                                return
                domainCount += 1
            return

        def restrictDomain(self, nodeDomain, value, subject, domainCount):
            count = 0
            for dictionaryDomain in nodeDomain:
                if count != domainCount:  # domain count represent the domain which i assign the value
                    if value in dictionaryDomain[subject]:  # if value exist in domain, delete it
                        dictionaryDomain[subject].remove(value)
                else:
                    for i in range(len(dictionaryDomain[subject]) - 1, -1, -1):
                        if dictionaryDomain[subject][i] != value:
                            del dictionaryDomain[subject][i]
                count += 1
            return True

        def checkConstraints(self, domain):
            for i in range(len(domain)):
                for constraint in self.constraints:
                    if constraint.constraintFunction(domain, i) == False:
                        return False

            return True

        def printResult(self, domain):
            keys = domain[0].keys()
            for key in keys:
                print(key, end = "  |  ")
            print("\n-----------------------")
            for subject in domain:
                for subjectKeys in subject.keys():
                    print(subject[subjectKeys][0], end=" | ")
                print("\n")


    print("The problems available in this directory: 1 2 3")
    input_no = input("Choose a problem: ")
    csp = CSPSolution(input_no)
    print("Here is the solution to the problem defined")
    csp.solveCSP()
