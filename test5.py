# unittest module for project euler problem 5
# smallest multiple 
import unittest
import smallmult 

class TestSmallMult(unittest.TestCase):
    def setUp(self):
        self.smallmult = smallmult.SmallMult()

    def testInitial(self):
        self.smallMult.setDigits(2)
        self.smallMult.calcMaxProd()
        assert self.smallMult.getMult() == (2520), "incorrect answer %d" % self.smallMult.getMult()

    def testFinal(self):
        self.smallMult.setDigits(3)
        self.smallMult.calcMaxProd()
        assert self.smallMult.getMult() == (0), "incorrect answer %d" % self.smallMult.getMult()

smallMultTestSuite = unittest.TestSuite()

smallMultTestSuite.addTest(TestSmallMult("testInitial"))
smallMultTestSuite.addTest(TestSmallMult("testFinal"))

runner = unittest.TextTestRunner()
runner.run(smallMultTestSuite)
