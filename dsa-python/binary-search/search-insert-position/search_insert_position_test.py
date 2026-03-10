import unittest

from search_insert_position import Solution


class TestSearchInsertPosition(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_found_middle(self):
        nums = [1, 3, 5, 6]
        self.assertEqual(self.s.searchInsert(nums, 5), 2)

    def test_found_left(self):
        nums = [1, 3, 5, 6]
        self.assertEqual(self.s.searchInsert(nums, 1), 0)

    def test_found_right(self):
        nums = [1, 3, 5, 6]
        self.assertEqual(self.s.searchInsert(nums, 6), 3)

    def test_insert_at_start(self):
        nums = [1, 3, 5, 6]
        self.assertEqual(self.s.searchInsert(nums, 0), 0)

    def test_insert_in_middle(self):
        nums = [1, 3, 5, 6]
        self.assertEqual(self.s.searchInsert(nums, 2), 1)

    def test_insert_at_end(self):
        nums = [1, 3, 5, 6]
        self.assertEqual(self.s.searchInsert(nums, 7), 4)

    def test_single_element_found(self):
        nums = [10]
        self.assertEqual(self.s.searchInsert(nums, 10), 0)

    def test_single_element_not_found_before(self):
        nums = [10]
        self.assertEqual(self.s.searchInsert(nums, 5), 0)

    def test_single_element_not_found_after(self):
        nums = [10]
        self.assertEqual(self.s.searchInsert(nums, 15), 1)

    def test_two_elements_between(self):
        nums = [1, 4]
        self.assertEqual(self.s.searchInsert(nums, 3), 1)

    def test_negative_numbers(self):
        nums = [-10, -3, 0, 5, 9]
        self.assertEqual(self.s.searchInsert(nums, -4), 1)

    def test_repeated_values_target(self):
        nums = [1, 2, 2, 2, 3]
        result = self.s.searchInsert(nums, 2)
        self.assertIn(result, {1, 2, 3})


if __name__ == "__main__":
    unittest.main()
