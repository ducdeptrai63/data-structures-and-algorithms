import unittest

from maximum_product_subarray import Solution


class TestMaximumProductSubarray(unittest.TestCase):
    def test_single_positive(self):
        sol = Solution()
        self.assertEqual(sol.maxProduct([5]), 5)

    def test_single_negative(self):
        sol = Solution()
        self.assertEqual(sol.maxProduct([-7]), -7)

    def test_all_positives(self):
        sol = Solution()
        self.assertEqual(sol.maxProduct([1, 2, 3, 4]), 24)

    def test_all_negatives_even_count(self):
        sol = Solution()
        self.assertEqual(sol.maxProduct([-1, -2, -3, -4]), 24)

    def test_all_negatives_odd_count(self):
        sol = Solution()
        self.assertEqual(sol.maxProduct([-1, -2, -3]), 6)

    def test_contains_zero_splits_subarray(self):
        sol = Solution()
        self.assertEqual(sol.maxProduct([2, 3, 0, 4, 5]), 20)

    def test_zero_and_negatives(self):
        sol = Solution()
        self.assertEqual(sol.maxProduct([0, -2, 0, -1, -3]), 3)

    def test_mixed_with_negative_flip(self):
        sol = Solution()
        self.assertEqual(sol.maxProduct([2, -5, -2, -4, 3]), 24)

    def test_classic_example(self):
        sol = Solution()
        self.assertEqual(sol.maxProduct([2, 3, -2, 4]), 6)

    def test_multiple_max_subarrays(self):
        sol = Solution()
        self.assertEqual(sol.maxProduct([1, -2, -3, 0, 7, -8, -2]), 112)

    def test_large_magnitude_values(self):
        sol = Solution()
        self.assertEqual(sol.maxProduct([-10, -10, 5, 2]), 1000)

    def test_leading_zero(self):
        sol = Solution()
        self.assertEqual(sol.maxProduct([0, 2]), 2)

    def test_trailing_zero(self):
        sol = Solution()
        self.assertEqual(sol.maxProduct([2, -1, -2, 0]), 4)


if __name__ == "__main__":
    unittest.main()
