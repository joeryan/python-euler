
class Prob1():
    def __init__(self):
        self.maxNum = 0

    def setMax(self, maxNum):
        self.maxNum = maxNum
        print "The maximum number range is: %d" % self.maxNum

    def answer(self):
        total = 0;
        for number in range(1,self.maxNum):
            if number % 3 == 0:
                total += number
            elif number % 5 == 0:
                total += number
        return total 
