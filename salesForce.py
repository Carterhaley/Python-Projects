from SalesPerson import SalesPerson

class SalesForce:
    def __init__(self):

    #Getter
    def addData(self, filename):
       infile = open(filename, ’r’)
        employee = []
        for line in infile:
            employee.append(line)
            infile.close()
    
    def quotaReport(self, quota):
        self.name
        
        

    def topSalesPerson(self, name1):
        if type(name1) == str:
            self.name = name1

    def individualSales(self, aSale):
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
        
        ##rtn 0,1, or-1

