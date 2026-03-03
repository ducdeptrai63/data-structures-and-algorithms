import unittest

from house_robber import Solution


class TestHouseRobber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list_returns_zero(self):
        self.assertEqual(self.solution.rob([]), 0)

    def test_single_element(self):
        self.assertEqual(self.solution.rob([5]), 5)

    def test_two_elements_picks_max(self):
        self.assertEqual(self.solution.rob([2, 7]), 7)

    def test_classic_example(self):
        self.assertEqual(self.solution.rob([1, 2, 3, 1]), 4)

    def test_example_with_skip(self):
        self.assertEqual(self.solution.rob([2, 7, 9, 3, 1]), 12)

    def test_all_zeros(self):
        self.assertEqual(self.solution.rob([0, 0, 0, 0]), 0)

    def test_increasing_sequence(self):
        self.assertEqual(self.solution.rob([1, 2, 3, 4, 5, 6]), 12)

    def test_alternating_high_low(self):
        self.assertEqual(self.solution.rob([10, 1, 10, 1, 10]), 30)

    def test_large_values(self):
        self.assertEqual(self.solution.rob([1000, 1, 1, 1000]), 2000)

    def test_multiple_optimal_paths(self):
        self.assertEqual(self.solution.rob([2, 2, 2, 2]), 4)

    def test_longer_list(self):
        self.assertEqual(self.solution.rob([6, 7, 1, 30, 8, 2, 4]), 41)


if __name__ == "__main__":
    unittest.main()
