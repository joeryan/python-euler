import unittest
import prob1

class TestProb1(unittest.TestCase):
    def runTest(self):
        problem = Prob1(100)
        assert problem == (100), "incorrect answer %d" % problem

testCase = TestProb1()

runner = unittest.TextTestRunner()
runner.run(testCase)

