import unittest

from top_k_frequent_elements import Solution


class TestTopKFrequentElements(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_element(self):
        nums = [1]
        k = 1
        expected = [1]
        self.assertCountEqual(self.solution.topKFrequent(nums, k), expected)

    def test_all_elements_identical(self):
        nums = [2, 2, 2, 2, 2]
        k = 1
        expected = [2]
        self.assertCountEqual(self.solution.topKFrequent(nums, k), expected)

    def test_all_elements_distinct(self):
        nums = [1, 2, 3, 4, 5]
        k = 5
        expected = [1, 2, 3, 4, 5]
        self.assertCountEqual(self.solution.topKFrequent(nums, k), expected)

    def test_mixed_positive_and_negative_numbers(self):
        nums = [1, 1, 1, -2, -2, 3]
        k = 2
        expected = [1, -2]
        self.assertCountEqual(self.solution.topKFrequent(nums, k), expected)

    def test_large_input_size(self):
        nums = [1] * 5000 + [-1] * 3000 + [0] * 2000
        k = 2
        expected = [1, -1]
        self.assertCountEqual(self.solution.topKFrequent(nums, k), expected)

    def test_order_independence(self):
        nums = [4, 1, -1, 2, -1, 2, 3]
        k = 2
        expected = [-1, 2]
        self.assertCountEqual(self.solution.topKFrequent(nums, k), expected)


if __name__ == '__main__':
    unittest.main()
