class PalProd():
    def __init__(self):
        self.maxProd = 0
        self.maxNum = 9

    def setDigits(self, dig):
        self.maxNum = pow(10, dig) 
        
    def calcMaxProd(self):
        for i in range(1, self.maxNum):
            for j in range(1, self.maxNum):
                if str(i*j)  == str(i*j)[::-1] and self.maxProd < i*j:
                    self.maxProd = i*j

    def getMaxProd(self):
        return self.maxProd
