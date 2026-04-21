import unittest

from guess_number_higher_or_lower import Solution


class TestGuessNumberHigherOrLower(unittest.TestCase):
    def test_pick_min(self):
        """Test when the picked number is the minimum possible value (1)."""
        sol = Solution(1)
        self.assertEqual(sol.guessNumber(10), 1)

    def test_pick_max(self):
        """Test when the picked number is the maximum possible value matching n."""
        sol = Solution(10)
        self.assertEqual(sol.guessNumber(10), 10)

    def test_pick_middle(self):
        """Test when the picked number is in the middle of the range."""
        sol = Solution(6)
        self.assertEqual(sol.guessNumber(10), 6)

    def test_n_is_1(self):
        """Test the smallest legitimate range n=1, pick=1."""
        sol = Solution(1)
        self.assertEqual(sol.guessNumber(1), 1)

    def test_large_n_pick_min(self):
        """Test large n with minimum possible pick."""
        n = 2**31 - 1
        sol = Solution(1)
        self.assertEqual(sol.guessNumber(n), 1)

    def test_large_n_pick_max(self):
        """Test large n with maximum possible pick."""
        n = 2**31 - 1
        sol = Solution(n)
        self.assertEqual(sol.guessNumber(n), n)

    def test_large_n_pick_middle(self):
        """Test large n with a middle pick."""
        n = 2**31 - 1
        pick = n // 2
        sol = Solution(pick)
        self.assertEqual(sol.guessNumber(n), pick)


if __name__ == '__main__':
    unittest.main()
