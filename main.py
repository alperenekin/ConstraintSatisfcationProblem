
if __name__ == '__main__':

    # her CSP Node satranc tahtasinin o anki durumunu tutar. Tepedeki CSPNode bos bir tahtayi ifade eder
    class CSPNode:  # agac yapisi icinde bir dugum
        def __init__(self):
            self.parent = None  # ebeveyni
            self.children = []  # cocuklarinin listesi
            self.assignment = []  # o anki satranc tahtasi durumu # 0. eleman birinci satirda hangi sutunda vezir oldugunu ifade eder

        def addChildren(self, childNode):
            childNode.setParent(self)  # dugume bir cocuk eklendiginde cocugunun ebeveyni olarak bu dugumu ata
            self.children.append(childNode)  # dugumu cocuklar listesine ekle

        def setParent(self, parentNode):  # ebeveyn ata
            self.assignment.extend(parentNode.assignment)  # ebeveyn atadiginda ebeveynin o anki atama durumunu al
            self.parent = parentNode  # ebeveyn degiskenini ata

        def assign(self, value):  # siradaki satirin value sutununa vezir koy
            self.assignment.append(value)

        def getAssignments(self):
            return self.assignment

        def getChildren(self):
            return self.children


    class CSPPRoblem:
        def __init__(self, variable_number, domain, constraintFunctionGlobal):
            self.rootNode = CSPNode()  # bos bir satranc tahtasi
            self.variable_number = variable_number  # degisken sayisi
            self.domain = domain  # domain: degiskenlerin alabilecegi deger listesi
            self.g_func = constraintFunctionGlobal  # sinirlayici fonksiyon

        def solveCSP(self):
            self._solve(self.rootNode)
            return self.rootNode

        def _solve(self, node):
            for value in domain:  # domaindeki her deger icin
                if self.g_func(node.getAssignments(), value):  # bu atama mumkun mu?
                    newNode = CSPNode()  # mumkun olan atamalar icin yeni dugumler olustur
                    node.addChildren(newNode)  # su an uzerinde calistigimiz dugumun cocugu olarak ekle
                    newNode.assign(value)  # yeni dugumde mumkun olan atamayı gerceklestir
                    self._solve(newNode)  # olusan yeni dugum icin yeni cozumler ara


    n = 8  # kaclik satranc tahtasi
    domain = range(n)


    def globalConstraint(prevAssign, newlyAssigned):
        column_constraint = not newlyAssigned in prevAssign  # prevAssign listesi icinde newlyAssigned varsa False yoksa True dondur
        diagonal_constraint = True
        indexToAssign = len(prevAssign)  # yeni degerin indeksi
        for idx, prev in enumerate(prevAssign):
            # caprazlik kontrolu indexToAssign, newlyAssigned, idx ve prev arasinda gerseklesecek
            # bunu butun atanmis taslar icin yapacagimiz icin dongu kurduk
            if abs(newlyAssigned - prev) - abs(indexToAssign - idx) == 0:
                diagonal_constraint = False
        return column_constraint and diagonal_constraint


    csp = CSPPRoblem(n, domain, globalConstraint)
    rn = csp.solveCSP()

    solution = []


    def traverseNode(node):
        assg = node.getAssignments()  # butun dugumler icin satranc tahtasinin o anki durumunu al
        if len(assg) == n:
            solution.append(assg)  # eger 8 elemanli bir atamysa bu biz cozumdur
        for childNode in node.getChildren():
            traverseNode(childNode)  # cocuk dugumleri dolas


    traverseNode(rn)

    print(len(solution))


    # 92

    def visualize(arr):
        from pprint import pprint
        str_list = [[" " for k in range(len(arr))] for i in range(len(arr))]
        for idx, element in enumerate(arr):
            str_list[idx][element] = "V"
        pprint(str_list)


    visualize(solution[1])
    # Cikti
    """
    [['V', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', 'V', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'V'],
     [' ', ' ', 'V', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', ' ', 'V', ' '],
     [' ', ' ', ' ', 'V', ' ', ' ', ' ', ' '],
     [' ', 'V', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', 'V', ' ', ' ', ' ']]
     """