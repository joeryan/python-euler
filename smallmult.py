class SmallMult():
    def __init__(self):
        self.digits = 1
        self.smallMult = 1

    def setDigits(self, dig):
        self.digits = dig

    def calcSmallMult(self):
        found = False
        count = 1
        while not found:
            self.smallMult = self.digits * count
            for i in range (2, self.digits):
                if self.smallMult % i != 0:
                    break
                if i == self.digits - 1:
                    found = True
            count += 1

    def getMult(self):
        return self.smallMult
