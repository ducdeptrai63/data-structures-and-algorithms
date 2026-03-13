import unittest

from contains_duplicate_2 import Solution


class TestContainsDuplicate2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_true_within_k(self):
        nums = [1, 2, 3, 1]
        res = self.solution.containsNearbyDuplicate(nums, 3)
        self.assertTrue(res)

    def test_false_when_duplicate_outside_k(self):
        nums = [1, 2, 3, 1]
        res = self.solution.containsNearbyDuplicate(nums, 2)
        self.assertFalse(res)

    def test_no_duplicates(self):
        nums = [1, 2, 3, 4, 5]
        res = self.solution.containsNearbyDuplicate(nums, 3)
        self.assertFalse(res)

    def test_k_zero_always_false(self):
        nums = [1, 1]
        res = self.solution.containsNearbyDuplicate(nums, 0)
        self.assertFalse(res)

        nums = [1, 2, 1]
        res = self.solution.containsNearbyDuplicate(nums, 0)
        self.assertFalse(res)

    def test_adjacent_duplicate_k_one(self):
        nums = [5, 5]
        res = self.solution.containsNearbyDuplicate(nums, 1)
        self.assertTrue(res)

        nums = [1, 2, 2, 3]
        res = self.solution.containsNearbyDuplicate(nums, 1)
        self.assertTrue(res)

    def test_negative_numbers(self):
        nums = [-1, -2, -3, -1]
        res = self.solution.containsNearbyDuplicate(nums, 3)
        self.assertTrue(res)

        nums = [-1, -2, -3, -1]
        res = self.solution.containsNearbyDuplicate(nums, 2)
        self.assertFalse(res)

    def test_large_k_equals_len_minus_one(self):
        nums = [9, 8, 7, 6, 9]
        res = self.solution.containsNearbyDuplicate(nums, 4)
        self.assertTrue(res)

    def test_multiple_duplicates_first_hit(self):
        nums = [1, 2, 3, 1, 2, 3]
        res = self.solution.containsNearbyDuplicate(nums, 2)
        self.assertFalse(res)

        nums = [1, 2, 3, 1, 2, 3]
        res = self.solution.containsNearbyDuplicate(nums, 3)
        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()
