# find the largest prime factor of an integer

# find the factors that are prime
class LgPrime():
    def __init__(self):
        self.num = 0
        self.primes = []

    def setNumber(self, num):
        self.num = num

    def lgPrimeNum(self):
        self.primes = set(reduce(list.__add__,
            ([i, self.num//i] for i in range(1, int(self.num**0.5) + 1) if self.num % 1 == 0)))
        return max(self.primes)

# determine the largest
