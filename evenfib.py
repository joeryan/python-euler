class EvenFib():
	def __init__(self):
		self.terms = -1 
		self.maxVal = -1
		
	def setTerms(self, terms):
		self.terms = terms

	def setMaxVal(self, maxVal):
		self.maxVal = maxVal

	def evenFib(self):
		sumEvenFib = 0
		curr, follow = 1, 2
		while (sumEvenFib < self.maxVal or self.maxVal
		for num in range(1, terms):
			if curr % 2 == 0:
				sumEvenFib += curr
			curr, follow = follow, curr + follow
		return sumEvenFib
