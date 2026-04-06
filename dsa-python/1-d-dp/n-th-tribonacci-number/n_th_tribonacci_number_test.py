import unittest

from n_th_tribonacci_number import Solution


class TestNThTribonacciNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_edge_cases(self):
        """Test the base cases of the tribonacci sequence."""
        self.assertEqual(self.solution.tribonacci(0), 0)
        self.assertEqual(self.solution.tribonacci(1), 1)
        self.assertEqual(self.solution.tribonacci(2), 1)

    def test_typical_cases(self):
        """Test typical small numbers in the sequence."""
        self.assertEqual(self.solution.tribonacci(3), 2)
        self.assertEqual(self.solution.tribonacci(4), 4)
        self.assertEqual(self.solution.tribonacci(5), 7)
        self.assertEqual(self.solution.tribonacci(6), 13)
        self.assertEqual(self.solution.tribonacci(7), 24)

    def test_large_cases(self):
        """Test larger constraint cases to ensure result fits in 32-bit integer limits."""
        self.assertEqual(self.solution.tribonacci(25), 1389537)

        # Test max value constraint for n <= 37 and ensuring it is <= 2^31 - 1
        self.assertEqual(self.solution.tribonacci(37), 2082876103)


if __name__ == '__main__':
    unittest.main()
