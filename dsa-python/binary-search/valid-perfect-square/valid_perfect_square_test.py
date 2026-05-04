import unittest
import random
import math

from valid_perfect_square import Solution


class TestValidPerfectSquare(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_boundary_value_n_is_1(self):
        """Test the minimum boundary value n = 1."""
        self.assertTrue(self.solution.isPerfectSquare(1))

    def test_small_perfect_squares(self):
        """Test small perfect squares."""
        self.assertTrue(self.solution.isPerfectSquare(4))
        self.assertTrue(self.solution.isPerfectSquare(9))
        self.assertTrue(self.solution.isPerfectSquare(16))
        self.assertTrue(self.solution.isPerfectSquare(25))

    def test_small_non_perfect_squares(self):
        """Test small non-perfect squares."""
        self.assertFalse(self.solution.isPerfectSquare(2))
        self.assertFalse(self.solution.isPerfectSquare(3))
        self.assertFalse(self.solution.isPerfectSquare(5))
        self.assertFalse(self.solution.isPerfectSquare(10))

    def test_large_perfect_squares(self):
        """Test large perfect squares near the upper bound (2^31 - 1)."""
        # Upper bound constraint is 2^31 - 1 = 2147483647
        # The largest perfect square <= 2147483647 is 46340^2 = 2147395600
        self.assertTrue(self.solution.isPerfectSquare(2147395600))
        self.assertTrue(self.solution.isPerfectSquare(46339 * 46339))
        self.assertTrue(self.solution.isPerfectSquare(40000 * 40000))

    def test_large_non_perfect_squares(self):
        """Test large non-perfect squares near the upper bound."""
        # 2^31 - 1
        self.assertFalse(self.solution.isPerfectSquare(2147483647))
        # Just above and below the largest perfect square
        self.assertFalse(self.solution.isPerfectSquare(
            2147395601))  # 46340^2 + 1
        self.assertFalse(self.solution.isPerfectSquare(
            2147395599))  # 46340^2 - 1

    def test_random_valid_values(self):
        """Test with random valid values."""
        random.seed(42)  # Fixed seed for determinism
        for _ in range(100):
            num = random.randint(1, 2**31 - 1)
            # Use math.isqrt to reliably check for perfect squares
            root = math.isqrt(num)
            expected = (root * root == num)
            self.assertEqual(self.solution.isPerfectSquare(
                num), expected, f"Failed on random value: {num}")


if __name__ == "__main__":
    unittest.main()
