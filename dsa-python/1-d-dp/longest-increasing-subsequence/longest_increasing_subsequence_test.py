import random
import unittest

from longest_increasing_subsequence import Solution


def lis_n2(nums):
    n = len(nums)
    if n == 0:
        return 0

    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


class TestLongestIncreasingSubsequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list_returns_zero(self):
        self.assertEqual(self.solution.lengthOfLIS([]), 0)

    def test_single_element_returns_one(self):
        self.assertEqual(self.solution.lengthOfLIS([42]), 1)

    def test_strictly_increasing_returns_length(self):
        nums = [1, 2, 3, 4, 5, 6]
        self.assertEqual(self.solution.lengthOfLIS(nums), 6)

    def test_strictly_decreasing_returns_one(self):
        nums = [6, 5, 4, 3, 2, 1]
        self.assertEqual(self.solution.lengthOfLIS(nums), 1)

    def test_all_equal_returns_one(self):
        nums = [7, 7, 7, 7, 7]
        self.assertEqual(self.solution.lengthOfLIS(nums), 1)

    def test_with_duplicates_strict_increase_required(self):
        nums = [1, 1, 2, 2, 3, 3]
        self.assertEqual(self.solution.lengthOfLIS(nums), 3)

    def test_canonical_example_1(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        self.assertEqual(self.solution.lengthOfLIS(nums), 4)

    def test_canonical_example_2(self):
        nums = [0, 1, 0, 3, 2, 3]
        self.assertEqual(self.solution.lengthOfLIS(nums), 4)

    def test_negative_numbers_and_duplicates(self):
        nums = [-1, -2, -3, -2, -1, -1, 0]
        self.assertEqual(self.solution.lengthOfLIS(nums), 4)

    def test_mixed_values_known_answer(self):
        nums = [3, 4, -1, 0, 6, 2, 3]
        self.assertEqual(self.solution.lengthOfLIS(nums), 4)

    def test_more_corner_cases(self):
        cases = [
            ([2, 2, 2, 1], 1),
            ([1, 2, 2, 2, 3], 3),
            ([4, 10, 4, 3, 8, 9], 3),
            ([1, 3, 6, 7, 9, 4, 10, 5, 6], 6),
            ([5, 1, 6, 2, 3, 4], 4),
        ]

        for nums, expected in cases:
            with self.subTest(nums=nums):
                self.assertEqual(self.solution.lengthOfLIS(nums), expected)

    def test_randomized_matches_quadratic_reference(self):
        rng = random.Random(0)

        for _ in range(200):
            n = rng.randint(0, 50)
            nums = [rng.randint(-20, 20) for _ in range(n)]
            with self.subTest(nums=nums):
                self.assertEqual(self.solution.lengthOfLIS(nums), lis_n2(nums))


if __name__ == "__main__":
    unittest.main()
