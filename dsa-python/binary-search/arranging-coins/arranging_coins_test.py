import unittest

from arranging_coins import Solution


class TestArrangingCoins(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minimum_n(self):
        self.assertEqual(self.solution.arrangeCoins(1), 1)

    def test_small_n(self):
        self.assertEqual(self.solution.arrangeCoins(2), 1)
        self.assertEqual(self.solution.arrangeCoins(3), 2)
        self.assertEqual(self.solution.arrangeCoins(4), 2)
        self.assertEqual(self.solution.arrangeCoins(5), 2)
        self.assertEqual(self.solution.arrangeCoins(6), 3)
        self.assertEqual(self.solution.arrangeCoins(8), 3)

    def test_exact_triangle_numbers(self):
        # 1+2+3+4 = 10
        self.assertEqual(self.solution.arrangeCoins(10), 4)
        # 1+2+3+4+5 = 15
        self.assertEqual(self.solution.arrangeCoins(15), 5)
        # 1+2+...+10 = 55
        self.assertEqual(self.solution.arrangeCoins(55), 10)

    def test_one_less_than_triangle_numbers(self):
        self.assertEqual(self.solution.arrangeCoins(9), 3)
        self.assertEqual(self.solution.arrangeCoins(14), 4)
        self.assertEqual(self.solution.arrangeCoins(54), 9)

    def test_maximum_n(self):
        # Maximum limit 2^31 - 1
        n = (1 << 31) - 1
        self.assertEqual(self.solution.arrangeCoins(n), 65535)

    def test_large_exact_triangle(self):
        # Triangle number for k = 65535 is 65535 * 65536 // 2 = 2147450880
        self.assertEqual(self.solution.arrangeCoins(2147450880), 65535)

    def test_large_one_less_than_triangle(self):
        # One less than the triangle number for k = 65535
        self.assertEqual(self.solution.arrangeCoins(2147450879), 65534)


if __name__ == '__main__':
    unittest.main()
