import unittest

from concatenation_of_array import Solution


class TestGetConcatenation(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minimum_length_input(self):
        nums = [1]
        expected = [1, 1]
        self.assertEqual(self.solution.getConcatenation(nums), expected)

    def test_maximum_length_input(self):
        nums = [1000] * 1000
        expected = [1000] * 2000
        self.assertEqual(self.solution.getConcatenation(nums), expected)

    def test_repeated_values(self):
        nums = [7, 7, 7, 7]
        expected = [7, 7, 7, 7, 7, 7, 7, 7]
        self.assertEqual(self.solution.getConcatenation(nums), expected)

    def test_distinct_values(self):
        nums = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
        self.assertEqual(self.solution.getConcatenation(nums), expected)

    def test_random_valid_inputs(self):
        nums = [4, 2, 9, 1, 5, 1000]
        expected = [4, 2, 9, 1, 5, 1000, 4, 2, 9, 1, 5, 1000]
        self.assertEqual(self.solution.getConcatenation(nums), expected)


if __name__ == '__main__':
    unittest.main()
