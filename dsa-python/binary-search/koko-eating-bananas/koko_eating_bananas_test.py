import unittest

from koko_eating_bananas import Solution


class TestKokoEatingBananas(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minimum_constraints(self):
        # piles.length = 1, h = 1, piles[i] = 1
        self.assertEqual(self.solution.minEatingSpeed([1], 1), 1)

    def test_single_pile(self):
        self.assertEqual(self.solution.minEatingSpeed([10], 5), 2)
        self.assertEqual(self.solution.minEatingSpeed([10], 10), 1)
        self.assertEqual(self.solution.minEatingSpeed([10], 1), 10)

    def test_h_equals_piles_length(self):
        # Koko can eat at most one pile per hour, so if h == len(piles),
        # the speed must be the max pile.
        self.assertEqual(self.solution.minEatingSpeed([3, 6, 7, 11], 4), 11)

    def test_very_large_pile_values(self):
        self.assertEqual(self.solution.minEatingSpeed(
            [1000000000], 2), 500000000)
        self.assertEqual(self.solution.minEatingSpeed(
            [1000000000, 1000000000], 3), 1000000000)

    def test_typical_cases(self):
        self.assertEqual(self.solution.minEatingSpeed([3, 6, 7, 11], 8), 4)
        self.assertEqual(self.solution.minEatingSpeed(
            [30, 11, 23, 4, 20], 5), 30)
        self.assertEqual(self.solution.minEatingSpeed(
            [30, 11, 23, 4, 20], 6), 23)

    def test_large_input_cases(self):
        # Large length, small elements
        piles = [1] * 1000
        self.assertEqual(self.solution.minEatingSpeed(piles, 1000000), 1)
        self.assertEqual(self.solution.minEatingSpeed(piles, 1000), 1)

        # Large length, large elements
        piles2 = [1000000000] * 1000
        self.assertEqual(self.solution.minEatingSpeed(
            piles2, 1000), 1000000000)


if __name__ == '__main__':
    unittest.main()
