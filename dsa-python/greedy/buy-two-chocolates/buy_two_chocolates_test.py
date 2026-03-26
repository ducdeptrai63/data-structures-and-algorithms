import unittest

from buy_two_chocolates import Solution


class TestBuyTwoChocolates(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_picks_two_cheapest_unsorted(self):
        prices = [3, 2, 5, 1]
        money = 7
        res = self.solution.buyChoco(prices, money)
        self.assertEqual(res, 4)  # buy 1 + 2 = 3, leftover 4

    def test_returns_money_when_cannot_afford_two_cheapest(self):
        prices = [4, 5, 6]
        money = 3
        res = self.solution.buyChoco(prices, money)
        self.assertEqual(res, 3)

    def test_leftover_zero_when_exact_afford(self):
        prices = [1, 2, 10]
        money = 3
        res = self.solution.buyChoco(prices, money)
        self.assertEqual(res, 0)

    def test_handles_duplicate_minimums(self):
        prices = [2, 2, 3]
        money = 5
        res = self.solution.buyChoco(prices, money)
        self.assertEqual(res, 1)

    def test_exactly_two_prices(self):
        prices = [5, 1]
        money = 10
        res = self.solution.buyChoco(prices, money)
        self.assertEqual(res, 4)

    def test_two_cheapest_not_first_two(self):
        prices = [8, 7, 1, 2]
        money = 6
        res = self.solution.buyChoco(prices, money)
        self.assertEqual(res, 3)

    def test_does_not_modify_input_list(self):
        prices = [9, 1, 6, 2, 2, 15, 3, 8]
        prices_before = prices[:]
        money = 7
        _ = self.solution.buyChoco(prices, money)
        self.assertEqual(prices, prices_before)

    def test_matches_reference_computation(self):
        prices = [9, 1, 6, 2, 2, 15, 3, 8]
        money = 7

        sorted_prices = sorted(prices)
        expected_leftover = money - (sorted_prices[0] + sorted_prices[1])
        expected = expected_leftover if expected_leftover >= 0 else money

        res = self.solution.buyChoco(prices, money)
        self.assertEqual(res, expected)

    def test_empty_prices_returns_money(self):
        prices = []
        money = 10
        res = self.solution.buyChoco(prices, money)

        # Implementation leaves min1/min2 as +inf and returns money.
        self.assertEqual(res, 10)

    def test_single_price_returns_money(self):
        prices = [5]
        money = 10
        res = self.solution.buyChoco(prices, money)
        self.assertEqual(res, 10)

    def test_negative_prices(self):
        prices = [-5, 2, -1, 10]
        money = 1
        res = self.solution.buyChoco(prices, money)
        # Two cheapest are -5 and -1 => cost -6 => leftover 7
        self.assertEqual(res, 7)

    def test_money_negative(self):
        prices = [1, 2, 3]
        money = -1
        res = self.solution.buyChoco(prices, money)
        # leftover = -1 - 3 = -4, not affordable => returns original money
        self.assertEqual(res, -1)

    def test_exception_prices_is_none(self):
        with self.assertRaises(TypeError):
            self.solution.buyChoco(None, 10)  # type: ignore[arg-type]

    def test_exception_money_is_not_int(self):
        with self.assertRaises(TypeError):
            self.solution.buyChoco([1, 2, 3], "10")  # type: ignore[arg-type]

    def test_exception_prices_contains_non_numeric(self):
        with self.assertRaises(TypeError):
            self.solution.buyChoco([1, "2", 3], 10)  # type: ignore[list-item]


if __name__ == '__main__':
    unittest.main()
