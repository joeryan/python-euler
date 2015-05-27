import unittest
import evenfib 

class TestEvenFib(unittest.TestCase):
    def setUp(self):
        self.evenFib = evenFib.evenFib()

    def testInitial(self):
        self.evenFib.setTerms(10)
        assert self.evenFib.answer() == (44), "incorrect answer %d" % evenFib.answer()

    def testFinal(self):
        self.evenFib.setMaxVal(4000000)
        assert self.evenFib.answer() == (233168), "incorrect answer %d" % self.evenFib.answer()

evenFibTestSuite = unittest.TestSuite()

evenFibTestSuite.addTest(TestEvenFib("testInitial"))
evenFibTestSuite.addTest(TestEvenFib("testFinal"))

runner = unittest.TextTestRunner()
runner.run(evenFibTestSuite)
