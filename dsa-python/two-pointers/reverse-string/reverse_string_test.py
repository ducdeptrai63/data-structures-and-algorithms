import unittest

from reverse_string import Solution


class TestReverseString(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_min_length_string(self):
        s = ["x"]
        self.solution.reverseString(s)
        self.assertEqual(s, ["x"])

    def test_empty_string(self):
        s = []
        self.solution.reverseString(s)
        self.assertEqual(s, [])

    def test_printable_ascii(self):
        s = list("a1@ B2# c3$")
        expected = list("$3c #2B @1a")
        self.solution.reverseString(s)
        self.assertEqual(s, expected)

    def test_large_string(self):
        s = list("A" * 50000 + "B" * 50000)
        expected = list("B" * 50000 + "A" * 50000)
        self.solution.reverseString(s)
        self.assertEqual(s, expected)

    def test_even_length(self):
        s = ["H", "a", "n", "n", "a", "h"]
        expected = ["h", "a", "n", "n", "a", "H"]
        self.solution.reverseString(s)
        self.assertEqual(s, expected)

    def test_odd_length(self):
        s = ["h", "e", "l", "l", "o"]
        expected = ["o", "l", "l", "e", "h"]
        self.solution.reverseString(s)
        self.assertEqual(s, expected)


if __name__ == '__main__':
    unittest.main()
