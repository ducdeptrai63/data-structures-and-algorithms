import unittest

from best_time_to_buy_and_sell_stock import Solution


class TestBestTimeToBuyAndSellStock(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_increasing_prices(self):
        prices = [1, 2, 3, 4, 5]
        res = self.solution.maxProfit(prices)
        self.assertEqual(res, 4)

    def test_decreasing_prices(self):
        prices = [7, 6, 4, 3, 1]
        res = self.solution.maxProfit(prices)
        self.assertEqual(res, 0)

    def test_single_element(self):
        prices = [5]
        res = self.solution.maxProfit(prices)
        self.assertEqual(res, 0)

    def test_two_elements_profit(self):
        prices = [1, 5]
        res = self.solution.maxProfit(prices)
        self.assertEqual(res, 4)

    def test_two_elements_no_profit(self):
        prices = [5, 1]
        res = self.solution.maxProfit(prices)
        self.assertEqual(res, 0)

    def test_mixed_case(self):
        prices = [7, 1, 5, 3, 6, 4]
        res = self.solution.maxProfit(prices)
        self.assertEqual(res, 5)

    def test_flat_prices(self):
        prices = [3, 3, 3, 3]
        res = self.solution.maxProfit(prices)
        self.assertEqual(res, 0)

    def test_late_best_peak(self):
        prices = [2, 4, 1, 7]
        res = self.solution.maxProfit(prices)
        self.assertEqual(res, 6)

    def test_large_drop_then_rise(self):
        prices = [10, 1, 2, 3, 0, 9]
        res = self.solution.maxProfit(prices)
        self.assertEqual(res, 9)

    def test_multiple_peaks(self):
        prices = [3, 8, 2, 5, 1, 7, 4, 9]
        res = self.solution.maxProfit(prices)
        self.assertEqual(res, 8)


if __name__ == '__main__':
    unittest.main()
