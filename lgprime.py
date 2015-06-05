# find the largest prime factor of an integer

# find the factors that are prime
class LgPrime():
    def __init__(self):
        self.num = 0
        self.primes = []

    def setNumber(self, num):
        self.num = num

    def lgPrimeNum(self):
        self.maxPrime = self.num
        i = 2
        while i * i < self.maxPrime:
            if self.maxPrime % i == 0:
                self.maxPrime = self.maxPrime / i
            i += 1
        return self.maxPrime

# determine the largest
