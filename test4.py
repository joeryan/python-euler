# unittest module for project euler problem 4
# palindrome products
import unittest
import palprod 

class TestPalinProd(unittest.TestCase):
    def setUp(self):
        self.palProd = palprod.PalProd()

    def testInitial(self):
        self.palProd.setDigits(2)
        self.palProd.calcMaxProd()
        assert self.palProd.getMaxProd() == (9009), "incorrect answer %d" % self.palProd.getMaxProd()

    def testFinal(self):
        self.palProd.setDigits(3)
        self.palProd.calcMaxProd()
        assert self.palProd.getMaxProd() == (906609), "incorrect answer %d" % self.palProd.getMaxProd()

palProdTestSuite = unittest.TestSuite()

palProdTestSuite.addTest(TestPalinProd("testInitial"))
palProdTestSuite.addTest(TestPalinProd("testFinal"))

runner = unittest.TextTestRunner()
runner.run(palProdTestSuite)
