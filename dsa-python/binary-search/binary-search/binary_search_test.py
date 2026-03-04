import unittest

from binary_search import Solution


class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_found_in_middle(self):
        nums = [1, 3, 5, 7, 9]
        self.assertEqual(self.solution.search(nums, 5), 2)

    def test_found_left_boundary(self):
        nums = [2, 4, 6, 8, 10]
        self.assertEqual(self.solution.search(nums, 2), 0)

    def test_found_right_boundary(self):
        nums = [2, 4, 6, 8, 10]
        self.assertEqual(self.solution.search(nums, 10), 4)

    def test_not_found_within_range(self):
        nums = [1, 3, 5, 7, 9]
        self.assertEqual(self.solution.search(nums, 6), -1)

    def test_empty_list(self):
        nums = []
        self.assertEqual(self.solution.search(nums, 1), -1)

    def test_single_element_found(self):
        nums = [7]
        self.assertEqual(self.solution.search(nums, 7), 0)

    def test_single_element_not_found(self):
        nums = [7]
        self.assertEqual(self.solution.search(nums, 5), -1)

    def test_negative_and_positive_values(self):
        nums = [-10, -3, 0, 4, 8, 12]
        self.assertEqual(self.solution.search(nums, -10), 0)
        self.assertEqual(self.solution.search(nums, 0), 2)
        self.assertEqual(self.solution.search(nums, 12), 5)
        self.assertEqual(self.solution.search(nums, -5), -1)

    def test_duplicates_any_valid_index(self):
        nums = [1, 2, 2, 2, 3]
        idx = self.solution.search(nums, 2)
        self.assertIn(idx, {1, 2, 3})


if __name__ == "__main__":
    unittest.main()
