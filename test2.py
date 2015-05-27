import unittest
import evenfib 

class TestEvenFib(unittest.TestCase):
    def setUp(self):
        self.evenFib = evenfib.EvenFib()

    def testInitial(self):
        self.evenFib.setTerms(10)
        assert self.evenFib.evenFibSum() == (44), "incorrect answer %d" % evenFib.evenFibSum()

    def testFinal(self):
        self.evenFib.setMaxVal(4000000)
        assert self.evenFib.evenFibSum() == (4613732), "incorrect answer %d" % self.evenFib.evenFibSum()

evenFibTestSuite = unittest.TestSuite()

evenFibTestSuite.addTest(TestEvenFib("testInitial"))
evenFibTestSuite.addTest(TestEvenFib("testFinal"))

runner = unittest.TextTestRunner()
runner.run(evenFibTestSuite)
