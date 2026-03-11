import unittest

from coin_change import Solution


class TestCoinChange(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_coin_change_basic(self):
        self.assertEqual(self.s.coinChange([1, 2, 5], 11), 3)

    def test_coin_change_impossible(self):
        self.assertEqual(self.s.coinChange([2], 3), -1)

    def test_coin_change_zero_amount(self):
        self.assertEqual(self.s.coinChange([1, 2, 5], 0), 0)

    def test_coin_change_single_coin_exact(self):
        self.assertEqual(self.s.coinChange([7], 14), 2)

    def test_coin_change_single_coin_impossible(self):
        self.assertEqual(self.s.coinChange([7], 13), -1)

    def test_coin_change_unsorted_coins(self):
        self.assertEqual(self.s.coinChange([5, 1, 2], 11), 3)

    def test_coin_change_duplicates(self):
        self.assertEqual(self.s.coinChange([1, 2, 2, 5], 4), 2)

    def test_coin_change_greedy_trap(self):
        self.assertEqual(self.s.coinChange([1, 3, 4], 6), 2)

    def test_coin_change_large_amount(self):
        self.assertEqual(self.s.coinChange([1, 3, 4], 100), 25)


if __name__ == "__main__":
    unittest.main()
