# unittest module for project euler problem 4
# palindrome products
import unittest
import palprod 

class TestPalinProd(unittest.TestCase):
    def setUp(self):
        self.palProd = palprod.PalProd()

    def testInitial(self):
        self.palProd.setDigits(2)
        self.palProd.calMaxProd()
        assert self.palProd.getMaxProd() == (29), "incorrect answer %d" % self.palProd.getMaxProd()

    def testFinal(self):
        self.palProd.setDigits(3)
        self.palProd.calcMaxProd()
        assert self.palProd.getMaxProd() == (6857), "incorrect answer %d" % self.palProd.getMaxProd()

palProdTestSuite = unittest.TestSuite()

palProdTestSuite.addTest(TestLargePrime("testInitial"))
palProdTestSuite.addTest(TestLargePrime("testFinal"))

runner = unittest.TextTestRunner()
runner.run(lgPrimeTestSuite)
