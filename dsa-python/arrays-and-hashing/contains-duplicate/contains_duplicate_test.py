import unittest

from contains_duplicate import Solution


class TestContainsDuplicate(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testExampleCase1(self):
        nums = [1, 2, 3, 1]
        res = self.solution.hasDuplicate(nums)
        self.assertTrue(res)

    def testExampleCase2(self):
        nums = [1, 2, 3, 4]
        res = self.solution.hasDuplicate(nums)
        self.assertFalse(res)

    def testExampleCase3(self):
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        res = self.solution.hasDuplicate(nums)
        self.assertTrue(res)

    def testSingleElement(self):
        nums = [1]
        res = self.solution.hasDuplicate(nums)
        self.assertFalse(res)

    def testTwoElementsDuplicate(self):
        nums = [2, 2]
        res = self.solution.hasDuplicate(nums)
        self.assertTrue(res)

    def testTwoElementsNotDuplicate(self):
        nums = [1, 2]
        res = self.solution.hasDuplicate(nums)
        self.assertFalse(res)

    def testEmptyArray(self):
        nums = []
        res = self.solution.hasDuplicate(nums)
        self.assertFalse(res)

    def testLargeArrayNoDuplicate(self):
        nums = list(range(10000))
        res = self.solution.hasDuplicate(nums)
        self.assertFalse(res)

    def testLargeArrayWithDuplicate(self):
        nums = list(range(10000)) + [9999]
        res = self.solution.hasDuplicate(nums)
        self.assertTrue(res)

    def testNegativeNumbers(self):
        nums = [-1, -2, -3, -1]
        res = self.solution.hasDuplicate(nums)
        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()
