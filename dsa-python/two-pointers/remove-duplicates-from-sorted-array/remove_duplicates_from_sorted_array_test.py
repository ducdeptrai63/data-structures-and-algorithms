import unittest

from remove_duplicates_from_sorted_array import Solution


class TestRemoveDuplicatesFromSortedArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def assert_result(self, nums, expected_unique):
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, len(expected_unique))
        self.assertEqual(nums[:k], expected_unique)
        for i in range(1, k):
            self.assertNotEqual(nums[i], nums[i - 1])

    def test_single_element(self):
        self.assert_result([5], [5])

    def test_all_unique(self):
        self.assert_result([1, 2, 3, 4], [1, 2, 3, 4])

    def test_all_duplicates(self):
        self.assert_result([7, 7, 7, 7], [7])

    def test_mixed_duplicates(self):
        self.assert_result([-2, -2, -1, -1, 0, 0, 1], [-2, -1, 0, 1])

    def test_clustered_duplicates(self):
        self.assert_result([0, 0, 1, 1, 1, 2, 3, 3], [0, 1, 2, 3])


if __name__ == "__main__":
    unittest.main()
