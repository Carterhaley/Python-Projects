## Name: J. Carter Haley, 8 December 2016

class SalesPerson:
    def __init__(self, idNum, name, sales):
        self.idNum = 0
        self.name = ""
        self.sales = []

    #Getter
    def getId(self, idNum):
        return self.idNum

    def getName(self, name):
        return self.name

    def setName(self, name1):
        if type(name1) == str:
            self.name = name1

    def enterSale(self, aSale):
        self.sales.append(aSale)
        return self.sales
    def totalSales(self):
        salesSum = 0
        for sale in self.sales:
            salesSum += sale
        return salesSum

    def getSales(self):
        return self.sales

    def metQuota(self, quota):
        quotaMet = False
        if self.totalSales() >= quota:
            quotaMet = True

    def compareTo(self, otherPerson):
        if self.totalSales() > otherPerson.totalSales():
            return 1
        elif self.totalSales() == otherPerson.totalSales():
            return 0
        elif self.totalSales() < otherPerson.totalSales():
            return -1

    def __str__(self):
        rtnStr = "ID: " + str(self.idNum) + "\nName: " + str(self.name)
        rtnStr += "\nTotal Sales: " + str(self.totalSales())
        return rtnStr
