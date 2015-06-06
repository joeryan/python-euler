# unittest module for project euler problem 5
# smallest multiple 
import unittest
import smallmult 

class TestSmallMult(unittest.TestCase):
    def setUp(self):
        self.smallMult = smallmult.SmallMult()

    def testInitial(self):
        self.smallMult.setDigits(10)
        self.smallMult.calcSmallMult()
        assert self.smallMult.getMult() == (2520), "incorrect answer %d" % self.smallMult.getMult()

    def testFinal(self):
        self.smallMult.setDigits(20)
        self.smallMult.calcSmallMult()
        assert self.smallMult.getMult() == (0), "incorrect answer %d" % self.smallMult.getMult()

smallMultTestSuite = unittest.TestSuite()

smallMultTestSuite.addTest(TestSmallMult("testInitial"))
smallMultTestSuite.addTest(TestSmallMult("testFinal"))

runner = unittest.TextTestRunner()
runner.run(smallMultTestSuite)
