import unittest

from search_in_rotated_sorted_array import Solution


class TestSearchInRotatedSortedArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_target_exists(self):
        self.assertEqual(self.solution.search([4, 5, 6, 7, 0, 1, 2], 0), 4)
        self.assertEqual(self.solution.search([4, 5, 6, 7, 0, 1, 2], 2), 6)
        self.assertEqual(self.solution.search([4, 5, 6, 7, 0, 1, 2], 4), 0)
        self.assertEqual(self.solution.search([4, 5, 6, 7, 0, 1, 2], 7), 3)

    def test_target_does_not_exist(self):
        self.assertEqual(self.solution.search([4, 5, 6, 7, 0, 1, 2], 3), -1)
        self.assertEqual(self.solution.search([4, 5, 6, 7, 0, 1, 2], 8), -1)
        self.assertEqual(self.solution.search([4, 5, 6, 7, 0, 1, 2], -1), -1)

    def test_array_size_one(self):
        self.assertEqual(self.solution.search([1], 1), 0)
        self.assertEqual(self.solution.search([1], 0), -1)
        self.assertEqual(self.solution.search([1], 2), -1)

    def test_array_not_rotated(self):
        self.assertEqual(self.solution.search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(self.solution.search([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(self.solution.search([1, 2, 3, 4, 5], 1), 0)
        self.assertEqual(self.solution.search([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(self.solution.search([1, 2, 3, 4, 5], 0), -1)

    def test_rotated_at_different_pivots(self):
        self.assertEqual(self.solution.search([2, 3, 4, 5, 1], 1), 4)
        self.assertEqual(self.solution.search([5, 1, 2, 3, 4], 5), 0)
        self.assertEqual(self.solution.search([5, 1, 2, 3, 4], 4), 4)
        self.assertEqual(self.solution.search([3, 1], 1), 1)
        self.assertEqual(self.solution.search([3, 1], 3), 0)
        self.assertEqual(self.solution.search([3, 1], 0), -1)
        self.assertEqual(self.solution.search([5, 1, 3], 5), 0)
        self.assertEqual(self.solution.search([5, 1, 3], 1), 1)
        self.assertEqual(self.solution.search([5, 1, 3], 3), 2)

    def test_target_is_pivot(self):
        self.assertEqual(self.solution.search([4, 5, 6, 7, 0, 1, 2], 0), 4)
        self.assertEqual(self.solution.search([7, 0, 1, 2, 4, 5, 6], 0), 1)

    def test_target_first_or_last(self):
        self.assertEqual(self.solution.search([4, 5, 6, 7, 0, 1, 2], 4), 0)
        self.assertEqual(self.solution.search([4, 5, 6, 7, 0, 1, 2], 2), 6)


if __name__ == '__main__':
    unittest.main()
