import unittest
import prob1

class TestProb1(unittest.TestCase):
    def setUp(self):
        self.prob1 = prob1.Prob1()

    def testInitial(self):
        self.prob1.setMax(10)
        assert self.prob1.answer() == (23), "incorrect answer %d" % prob1.answer()

    def testFinal(self):
        self.prob1.setMax(1000)
        assert self.prob1.answer() == (233168), "incorrect answer %d" % self.prob1.answer()

prob1TestSuite = unittest.TestSuite()

prob1TestSuite.addTest(TestProb1("testInitial"))
prob1TestSuite.addTest(TestProb1("testFinal"))

runner = unittest.TextTestRunner()
runner.run(prob1TestSuite)
