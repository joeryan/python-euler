import unittest
import lgprime 

class TestLargePrime(unittest.TestCase):
    def setUp(self):
        self.lgPrime = lgprime.LgPrime()

    def testInitial(self):
        self.lgPrime.setNumber(13195)
        assert self.lgPrime.lgPrimeNum() == (29), "incorrect answer %d" % self.lgPrime.lgPrimeNum()

    def testFinal(self):
        self.lgPrime.setNumber(600851475143)
        assert self.lgPrime.lgPrimeNum() == (6857), "incorrect answer %d" % self.lgPrime.lgPrimeNum()

lgPrimeTestSuite = unittest.TestSuite()

lgPrimeTestSuite.addTest(TestLargePrime("testInitial"))
lgPrimeTestSuite.addTest(TestLargePrime("testFinal"))

runner = unittest.TextTestRunner()
runner.run(lgPrimeTestSuite)
