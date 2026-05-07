import unittest

from sqrt_x import Solution


class TestSqrtX(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_zero(self):
        self.assertEqual(self.sol.mySqrt(0), 0)

    def test_one(self):
        self.assertEqual(self.sol.mySqrt(1), 1)

    def test_perfect_squares(self):
        self.assertEqual(self.sol.mySqrt(4), 2)
        self.assertEqual(self.sol.mySqrt(9), 3)
        self.assertEqual(self.sol.mySqrt(16), 4)
        self.assertEqual(self.sol.mySqrt(25), 5)
        self.assertEqual(self.sol.mySqrt(100), 10)

    def test_non_perfect_squares(self):
        self.assertEqual(self.sol.mySqrt(2), 1)
        self.assertEqual(self.sol.mySqrt(3), 1)
        self.assertEqual(self.sol.mySqrt(8), 2)
        self.assertEqual(self.sol.mySqrt(15), 3)
        self.assertEqual(self.sol.mySqrt(24), 4)
        self.assertEqual(self.sol.mySqrt(99), 9)

    def test_maximum_boundary(self):
        # Constraint: 0 <= x <= 2^31 - 1
        max_val = (1 << 31) - 1
        # floor(sqrt(2147483647)) = 46340
        self.assertEqual(self.sol.mySqrt(max_val), 46340)

    def test_large_values_near_square_boundaries(self):
        # 46340^2 = 2147395600
        # 46341^2 = 2147488281 (exceeds max_val)
        self.assertEqual(self.sol.mySqrt(2147395600), 46340)
        self.assertEqual(self.sol.mySqrt(2147395599), 46339)
        self.assertEqual(self.sol.mySqrt(2147395601), 46340)


if __name__ == '__main__':
    unittest.main()
