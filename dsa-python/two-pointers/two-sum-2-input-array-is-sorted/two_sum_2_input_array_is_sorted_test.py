import unittest

from two_sum_2_input_array_is_sorted import Solution


class TestTwoSum2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_standard_case(self):
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [1, 2])

    def test_minimum_length_array(self):
        self.assertEqual(self.solution.twoSum([2, 3], 5), [1, 2])

    def test_negative_numbers(self):
        self.assertEqual(self.solution.twoSum([-1, 0], -1), [1, 2])
        self.assertEqual(self.solution.twoSum(
            [-1000, -500, 0, 500, 1000], -1500), [1, 2])
        self.assertEqual(self.solution.twoSum(
            [-5, -4, -3, -2, -1], -8), [1, 3])

    def test_duplicate_values(self):
        self.assertEqual(self.solution.twoSum([0, 0], 0), [1, 2])
        self.assertEqual(self.solution.twoSum([3, 3], 6), [1, 2])
        self.assertEqual(self.solution.twoSum(
            [1, 2, 3, 4, 4, 9, 56, 90], 8), [4, 5])

    def test_target_formed_by_first_and_last_elements(self):
        self.assertEqual(self.solution.twoSum([1, 2, 3, 4, 5], 6), [1, 5])
        self.assertEqual(self.solution.twoSum([-1000, 0, 1000], 0), [1, 3])

    def test_large_array(self):
        # Array of length 30000 with a unique solution pair
        numbers = [1] * 14999 + [2, 3] + [5] * 14999
        self.assertEqual(self.solution.twoSum(numbers, 5), [15000, 15001])


if __name__ == '__main__':
    unittest.main()
