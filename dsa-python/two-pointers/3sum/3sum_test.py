import unittest

import importlib

# Dynamically import 3sum.py since module name starts with a digit
three_sum_module = importlib.import_module("3sum")
Solution = three_sum_module.Solution


class TestThreeSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def normalize(self, result):
        """
        Helper method to sort triplets internally and then sort the list of triplets
        to allow order-independent comparison.
        """
        return sorted([sorted(triplet) for triplet in result])

    def test_minimum_length_valid(self):
        nums = [-1, 0, 1]
        expected = [[-1, 0, 1]]
        result = self.solution.threeSum(nums)
        self.assertEqual(self.normalize(result), self.normalize(expected))

    def test_minimum_length_invalid(self):
        nums = [1, 2, 3]
        expected = []
        result = self.solution.threeSum(nums)
        self.assertEqual(self.normalize(result), self.normalize(expected))

    def test_multiple_valid_triplets(self):
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, -1, 2], [-1, 0, 1]]
        result = self.solution.threeSum(nums)
        self.assertEqual(self.normalize(result), self.normalize(expected))

    def test_no_valid_triplet(self):
        nums = [0, 1, 1]
        expected = []
        result = self.solution.threeSum(nums)
        self.assertEqual(self.normalize(result), self.normalize(expected))

    def test_mix_negative_positive_zero(self):
        nums = [-2, 0, 1, 1, 2]
        expected = [[-2, 0, 2], [-2, 1, 1]]
        result = self.solution.threeSum(nums)
        self.assertEqual(self.normalize(result), self.normalize(expected))

    def test_duplicate_elements(self):
        nums = [0, 0, 0, 0]
        expected = [[0, 0, 0]]
        result = self.solution.threeSum(nums)
        self.assertEqual(self.normalize(result), self.normalize(expected))

    def test_large_valid_input(self):
        # 1000 elements conforming to constraints
        nums = [0] * 994 + [1, -1, 2, -2, 3, -3]
        expected = [
            [-3, 0, 3],
            [-3, 1, 2],
            [-2, -1, 3],
            [-2, 0, 2],
            [-1, 0, 1],
            [0, 0, 0]
        ]
        result = self.solution.threeSum(nums)
        self.assertEqual(self.normalize(result), self.normalize(expected))

    def test_extreme_values(self):
        nums = [-100000, 0, 100000]
        expected = [[-100000, 0, 100000]]
        result = self.solution.threeSum(nums)
        self.assertEqual(self.normalize(result), self.normalize(expected))


if __name__ == '__main__':
    unittest.main()
