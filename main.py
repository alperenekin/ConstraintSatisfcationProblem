import copy

from fileReader import FileReader

if __name__ == '__main__':
    class CSPNode:  # agac yapisi icinde bir dugum
        def __init__(self, domain):
            self.domain = domain

        def setDomain(self, domain):
            self.domain = domain

        def getDomains(self):
            return self.domains


    class CSPPRoblem:
        def __init__(self):
            fileReader = FileReader()
            data1 = fileReader.readDataFile("data-2.txt")
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

            self.rootNode = CSPNode(domains)  # bos bir satranc tahtasi
            self.constraints = fileReader.readClueFile("clues-2.txt")

        def isAllDomainsHaveOneElement(self, node):
            for dictionaryDomain in node.domain:  # domaindeki her deger icin
                for subject in dictionaryDomain:
                    if len(dictionaryDomain[subject]) != 1:
                        return False
            return True

        def isSolved(self, node):
            if self.isAllDomainsHaveOneElement(node) and self.checkConstraints(node.domain): # to check if answer passes from constraints
                print(node.domain)
                self.checkConstraints(node.domain)
                print("true")

        def solveCSP(self):
            self._solve(self.rootNode)
            return self.rootNode

        def _solve(self, node):
            self.isSolved(node)
            domainCount = 0
            elementCount = 0
            for dictionaryDomain in node.domain:  # domaindeki her deger icin
                for subject in dictionaryDomain:
                    if len(dictionaryDomain[subject]) > 1:
                        for values in dictionaryDomain[subject]:
                            elementCount += 1
                            if self.checkConstraints(node.domain):
                                child_domain = copy.deepcopy(node.domain)
                                childNode = CSPNode(child_domain)
                                self.restrictDomain(childNode.domain, values, subject, domainCount)
                                self._solve(childNode)
                            if elementCount == len(dictionaryDomain[subject]):
                                return False
                domainCount += 1
            return False

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


    csp = CSPPRoblem()
    rn = csp.solveCSP()
