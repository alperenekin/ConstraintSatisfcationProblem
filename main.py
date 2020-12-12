import copy

from fileReader import FileReader

if __name__ == '__main__':

    # her CSP Node satranc tahtasinin o anki durumunu tutar. Tepedeki CSPNode bos bir tahtayi ifade eder
    class CSPNode:  # agac yapisi icinde bir dugum
        def __init__(self, domain):
            self.parent = None  # ebeveyni
            self.children = []  # cocuklarinin listesi
            self.domain = domain
            self.answer = []  # o anki satranc tahtasi durumu # 0. eleman birinci satirda hangi sutunda vezir oldugunu ifade eder

        def addChildren(self, childNode):
            childNode.setParent(self)  # dugume bir cocuk eklendiginde cocugunun ebeveyni olarak bu dugumu ata
            self.children.append(childNode)  # dugumu cocuklar listesine ekle

        def setParent(self, parentNode):  # ebeveyn ata
            # self.domain.extend(parentNode.assignment)  # ebeveyn atadiginda ebeveynin o anki atama durumunu al
            self.parent = parentNode  # ebeveyn degiskenini ata

        def assign(self, value):  # siradaki satirin value sutununa vezir koy
            self.domain.append(value)

        def setDomain(self, domain):
            self.domain = domain

        def getDomains(self):
            return self.domains

        def getChildren(self):
            return self.children


    class CSPPRoblem:
        def __init__(self, constraints):
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
            self.rootNode = CSPNode(domains)  # bos bir satranc tahtasi
            self.constraints = constraints

        def solveCSP(self):
            self._solve(self.rootNode)
            return self.rootNode

        def _solve(self, node):
            newNode = CSPNode(node.domain)
            domainCount = 0
            for dictionaryDomain in newNode.domain:  # domaindeki her deger icin
                for subject in dictionaryDomain:
                    for values in dictionaryDomain[subject]:
                        self.restrictDomain(newNode.domain, values, subject, domainCount)
                domainCount += 1

        def restrictDomain(self,nodeDomain, value, subject, domainCount):
            count = 0
            for dictionaryDomain in nodeDomain:
                if (count != domainCount): #domain count represent the domain which i assign the value
                    if(value in dictionaryDomain[subject]): #if value exist in domain, delete it
                        dictionaryDomain[subject].remove(value)
                else:
                    for i in range(len(dictionaryDomain[subject]) - 1, -1, -1):
                        if dictionaryDomain[subject][i] != value:
                            del dictionaryDomain[subject][i]
                count += 1
                    # for element in dictionaryDomain[subject]:
                    #     if(element != value):
                    #         dictionaryDomain[subject].remove(element)


    # yeni node yaratıp, ona bir domain ve keyleri pasladı
    # Her bir subjecti dönüyor, mesela ilk years geldi ve onun ilk elemanını domainden sildi

    fileReader = FileReader()
    array = fileReader.readClueFile("clues-1.txt")
    csp = CSPPRoblem(array)
    rn = csp.solveCSP()
