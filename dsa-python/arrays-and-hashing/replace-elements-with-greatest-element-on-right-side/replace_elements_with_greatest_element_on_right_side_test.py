import unittest

from replace_elements_with_greatest_element_on_right_side import Solution


class TestReplaceElements(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minimum_size_array(self):
        arr = [10]
        expected = [-1]
        self.assertEqual(self.solution.replaceElements(arr.copy()), expected)

    def test_large_size_array(self):
        # A large array of 10,000 elements.
        # Using a pattern [1, 2, 1, 2, ...] where max to the right is always 2 (except the last element)
        arr = [1, 2] * 5000
        expected = [2] * 9999 + [-1]
        self.assertEqual(self.solution.replaceElements(arr.copy()), expected)

    def test_increasing_order_array(self):
        arr = [1, 2, 3, 4, 5]
        expected = [5, 5, 5, 5, -1]
        self.assertEqual(self.solution.replaceElements(arr.copy()), expected)

    def test_decreasing_order_array(self):
        arr = [5, 4, 3, 2, 1]
        expected = [4, 3, 2, 1, -1]
        self.assertEqual(self.solution.replaceElements(arr.copy()), expected)

    def test_random_values(self):
        arr = [17, 18, 5, 4, 6, 1]
        expected = [18, 6, 6, 6, 1, -1]
        self.assertEqual(self.solution.replaceElements(arr.copy()), expected)

        arr2 = [400, 22, 9, 33, 21, 50, 41, 60, 80, 1]
        expected2 = [80, 80, 80, 80, 80, 80, 80, 80, 1, -1]
        self.assertEqual(self.solution.replaceElements(arr2.copy()), expected2)

    def test_all_elements_equal(self):
        arr = [5, 5, 5, 5, 5]
        expected = [5, 5, 5, 5, -1]
        self.assertEqual(self.solution.replaceElements(arr.copy()), expected)


if __name__ == "__main__":
    unittest.main()
