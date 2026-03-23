import unittest

from find_the_town_judge import Solution


class TestFindTheTownJudge(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testNEquals1EmptyTrustReturns1(self):
        self.assertEqual(self.solution.findJudge(1, []), 1)

    def testNEquals2SingleTrustPairReturns2(self):
        self.assertEqual(self.solution.findJudge(2, [[1, 2]]), 2)

    def testSimpleJudgeIn3PeopleReturns3(self):
        trust = [[1, 3], [2, 3]]
        self.assertEqual(self.solution.findJudge(3, trust), 3)

    def testEmptyTrustWithNGreaterThan1ReturnsMinus1(self):
        self.assertEqual(self.solution.findJudge(2, []), -1)
        self.assertEqual(self.solution.findJudge(5, []), -1)

    def testMutualTrustNoJudge(self):
        self.assertEqual(self.solution.findJudge(2, [[1, 2], [2, 1]]), -1)

    def testCycleNoJudge(self):
        trust = [[1, 2], [2, 3], [3, 1]]
        self.assertEqual(self.solution.findJudge(3, trust), -1)

    def testCandidateTrustedByAllButTrustsSomeoneIsNotJudge(self):
        # Person 3 is trusted by 1 and 2, but person 3 trusts 2 => no judge.
        trust = [[1, 3], [2, 3], [3, 2]]
        self.assertEqual(self.solution.findJudge(3, trust), -1)

    def testJudgeExistsEvenWithAdditionalEdgesAmongOthers(self):
        # Judge = 3: trusted by 1,2,4 and trusts nobody; extra edge 1->2 shouldn't affect.
        trust = [[1, 3], [2, 3], [4, 3], [1, 2]]
        self.assertEqual(self.solution.findJudge(4, trust), 3)

    def testNoOneHasRequiredScoreNoJudge(self):
        trust = [[1, 2], [1, 3], [2, 1], [3, 2]]
        self.assertEqual(self.solution.findJudge(3, trust), -1)


if __name__ == '__main__':
    unittest.main()
