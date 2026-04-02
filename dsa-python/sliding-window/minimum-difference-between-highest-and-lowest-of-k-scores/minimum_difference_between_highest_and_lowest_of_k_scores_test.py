import random
import unittest

from minimum_difference_between_highest_and_lowest_of_k_scores import Solution


def reference_minimum_difference(nums, k):
    if k == 1:
        return 0
    arr = sorted(nums)
    best = arr[-1] - arr[0]
    for i in range(0, len(arr) - k + 1):
        best = min(best, arr[i + k - 1] - arr[i])
    return best


class TestMinimumDifferenceBetweenHighestAndLowestOfKScores(unittest.TestCase):
    def setUp(self):
        self.sut = Solution()

    def test_min_boundary_len1_k1(self):
        nums = [42]
        k = 1
        self.assertEqual(self.sut.minimumDifference(nums[:], k), 0)

    def test_k_equals_1_always_zero_various_inputs(self):
        cases = [
            [0],
            [5, 1, 9, 2],
            [100000, 0, 50000, 50000],
            [7, 7, 7, 7, 7],
            [3, 2, 1, 0],
        ]
        for nums in cases:
            with self.subTest(nums=nums):
                self.assertEqual(self.sut.minimumDifference(nums[:], 1), 0)

    def test_k_equals_length_returns_range(self):
        nums = [9, 1, 5, 3]
        k = len(nums)
        expected = max(nums) - min(nums)
        self.assertEqual(self.sut.minimumDifference(nums[:], k), expected)

    def test_general_unsorted_input(self):
        nums = [10, 1, 7, 4, 9]
        k = 3
        expected = reference_minimum_difference(nums, k)
        self.assertEqual(self.sut.minimumDifference(nums[:], k), expected)

    def test_general_with_duplicates(self):
        nums = [4, 4, 4, 7, 7, 10]
        k = 4
        expected = reference_minimum_difference(nums, k)
        self.assertEqual(self.sut.minimumDifference(nums[:], k), expected)

    def test_general_mixed_small_and_large_values(self):
        nums = [0, 100000, 2, 99999, 50, 50000]
        k = 2
        expected = reference_minimum_difference(nums, k)
        self.assertEqual(self.sut.minimumDifference(nums[:], k), expected)

    def test_all_elements_equal_any_k(self):
        nums = [12345] * 10
        for k in (1, 2, 5, 10):
            with self.subTest(k=k):
                self.assertEqual(self.sut.minimumDifference(nums[:], k), 0)

    def test_strictly_increasing_sequence(self):
        nums = list(range(0, 20))  # 0..19
        k = 5
        expected = reference_minimum_difference(nums, k)
        self.assertEqual(self.sut.minimumDifference(nums[:], k), expected)

    def test_strictly_decreasing_sequence(self):
        nums = list(range(50, 0, -1))  # 50..1
        k = 10
        expected = reference_minimum_difference(nums, k)
        self.assertEqual(self.sut.minimumDifference(nums[:], k), expected)

    def test_large_input_near_1000_random_values(self):
        rng = random.Random(123456)
        nums = [rng.randint(0, 100000) for _ in range(997)]
        k = 37
        expected = reference_minimum_difference(nums, k)
        self.assertEqual(self.sut.minimumDifference(nums[:], k), expected)

    def test_large_input_k_equals_length(self):
        rng = random.Random(999)
        nums = [rng.randint(0, 100000) for _ in range(1000)]
        k = len(nums)
        expected = max(nums) - min(nums)
        self.assertEqual(self.sut.minimumDifference(nums[:], k), expected)


if __name__ == "__main__":
    unittest.main()
