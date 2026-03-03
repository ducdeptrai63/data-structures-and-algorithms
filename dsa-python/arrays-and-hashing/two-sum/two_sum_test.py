import unittest

from two_sum import Solution


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def assert_valid_pair(self, nums, target, result):
        self.assertIsNotNone(result, "Expected a pair of indices, got None.")
        self.assertEqual(
            len(result), 2, "Result should contain exactly two indices.")
        i, j = result
        self.assertIsInstance(i, int)
        self.assertIsInstance(j, int)
        self.assertNotEqual(i, j, "Indices must be distinct.")
        self.assertTrue(0 <= i < len(nums))
        self.assertTrue(0 <= j < len(nums))
        self.assertEqual(nums[i] + nums[j], target)

    def test_basic_example(self):
        nums = [2, 7, 11, 15]
        target = 9
        result = self.solution.twoSum(nums, target)
        self.assert_valid_pair(nums, target, result)

    def test_pair_late_in_list(self):
        nums = [1, 3, 5, 7, 9]
        target = 16
        result = self.solution.twoSum(nums, target)
        self.assert_valid_pair(nums, target, result)

    def test_duplicates(self):
        nums = [3, 3]
        target = 6
        result = self.solution.twoSum(nums, target)
        self.assert_valid_pair(nums, target, result)

    def test_with_zeros(self):
        nums = [0, 4, 3, 0]
        target = 0
        result = self.solution.twoSum(nums, target)
        self.assert_valid_pair(nums, target, result)

    def test_all_negative(self):
        nums = [-1, -2, -3, -4, -5]
        target = -8
        result = self.solution.twoSum(nums, target)
        self.assert_valid_pair(nums, target, result)

    def test_mixed_signs(self):
        nums = [1, -2, 3, 7]
        target = 5
        result = self.solution.twoSum(nums, target)
        self.assert_valid_pair(nums, target, result)

    def test_minimal_length(self):
        nums = [5, 5]
        target = 10
        result = self.solution.twoSum(nums, target)
        self.assert_valid_pair(nums, target, result)

    def test_empty_list_returns_none(self):
        nums = []
        target = 1
        result = self.solution.twoSum(nums, target)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
