from sys import maxint

class EvenFib():
    
    def __init__(self):
	self.terms = maxint 
	self.maxVal = maxint 
		
    def setTerms(self, terms):
	self.terms = terms

    def setMaxVal(self, maxVal):
	self.maxVal = maxVal

    def evenFibSum(self):
	sumEvenFib, terms = 0, 1
	curr, follow = 1, 2
        while (sumEvenFib < self.maxVal and terms < self.terms):
            if curr % 2 == 0:
                sumEvenFib += curr
            curr, follow = follow, curr + follow
            terms += 1
        return sumEvenFib
