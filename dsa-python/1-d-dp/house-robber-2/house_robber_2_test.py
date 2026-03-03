import unittest

from house_robber_2 import Solution


class TestHouseRobberII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_house(self):
        self.assertEqual(self.solution.rob([7]), 7)

    def test_two_houses(self):
        self.assertEqual(self.solution.rob([2, 9]), 9)

    def test_circular_conflict_basic(self):
        self.assertEqual(self.solution.rob([2, 3, 2]), 3)

    def test_circular_conflict_longer(self):
        self.assertEqual(self.solution.rob([1, 2, 3, 1]), 4)

    def test_excluding_first_is_better(self):
        self.assertEqual(self.solution.rob([4, 1, 2, 7, 5, 3, 1]), 14)

    def test_excluding_last_is_better(self):
        self.assertEqual(self.solution.rob([10, 2, 3, 7, 1]), 17)

    def test_all_zeros(self):
        self.assertEqual(self.solution.rob([0, 0, 0, 0]), 0)

    def test_alternating_high_low(self):
        self.assertEqual(self.solution.rob([10, 1, 10, 1, 10]), 20)

    def test_large_values(self):
        self.assertEqual(self.solution.rob([100, 1, 1, 100]), 101)


if __name__ == "__main__":
    unittest.main()
