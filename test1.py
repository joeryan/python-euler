import unittest
import prob1

class TestProb1(unittest.TestCase):
    def runTest(self):
        problem = prob1.Prob1(10)
        assert problem.answer() == (23), "incorrect answer %d" % problem.answer()

testCase = TestProb1()

runner = unittest.TextTestRunner()
runner.run(testCase)

