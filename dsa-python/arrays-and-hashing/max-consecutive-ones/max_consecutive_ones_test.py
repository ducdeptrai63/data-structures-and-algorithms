import unittest
import random

from max_consecutive_ones import Solution


class TestMaxConsecutiveOnes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_edge_cases(self):
        """Test with minimum length constraints and small arrays."""
        self.assertEqual(self.solution.findMaxConsecutiveOnes([0]), 0)
        self.assertEqual(self.solution.findMaxConsecutiveOnes([1]), 1)
        self.assertEqual(self.solution.findMaxConsecutiveOnes([1, 1]), 2)
        self.assertEqual(self.solution.findMaxConsecutiveOnes([0, 0]), 0)
        self.assertEqual(self.solution.findMaxConsecutiveOnes([1, 0]), 1)
        self.assertEqual(self.solution.findMaxConsecutiveOnes([0, 1]), 1)

    def test_all_zeros(self):
        """Test with an array containing only zeros."""
        self.assertEqual(self.solution.findMaxConsecutiveOnes([0] * 100), 0)

    def test_all_ones(self):
        """Test with an array containing only ones."""
        self.assertEqual(self.solution.findMaxConsecutiveOnes([1] * 100), 100)

    def test_alternating(self):
        """Test with arrays containing alternating patterns."""
        self.assertEqual(self.solution.findMaxConsecutiveOnes(
            [1, 0, 1, 0, 1, 0, 1]), 1)
        self.assertEqual(self.solution.findMaxConsecutiveOnes(
            [0, 1, 0, 1, 0, 1, 0]), 1)
        self.assertEqual(self.solution.findMaxConsecutiveOnes(
            [1, 1, 0, 1, 1, 0, 1, 1, 0]), 2)
        self.assertEqual(self.solution.findMaxConsecutiveOnes(
            [1, 1, 0, 1, 1, 1, 0, 1]), 3)

    def test_max_length_case(self):
        """Test with the maximum length constraint (100,000)."""
        n = 100000

        # All ones up to constraint
        self.assertEqual(self.solution.findMaxConsecutiveOnes([1] * n), n)

        # All zeros up to constraint
        self.assertEqual(self.solution.findMaxConsecutiveOnes([0] * n), 0)

        # Large array with a specific block of ones
        large_mixed = [0] * n
        # First block: length 49001
        for i in range(1000, 50001):
            large_mixed[i] = 1
        # Second block: length 20001
        for i in range(60000, 80001):
            large_mixed[i] = 1

        self.assertEqual(
            self.solution.findMaxConsecutiveOnes(large_mixed), 49001)

    def test_random_valid_cases(self):
        """Test with randomly generated valid cases and compare against a reference logic."""
        random.seed(42)  # For reproducibility
        for _ in range(10):
            n = random.randint(1000, 5000)
            nums = [random.choice([0, 1]) for _ in range(n)]

            # Independent reference logic to find max consecutive ones
            expected_max = 0
            current_max = 0
            for num in nums:
                if num == 1:
                    current_max += 1
                    expected_max = max(expected_max, current_max)
                else:
                    current_max = 0

            self.assertEqual(
                self.solution.findMaxConsecutiveOnes(nums), expected_max)


if __name__ == '__main__':
    unittest.main()
