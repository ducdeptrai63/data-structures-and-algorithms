import unittest

from permutation_in_string import Solution


class TestPermutationInString(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_positive(self):
        # Basic positive case (permutation exists)
        self.assertTrue(self.solution.checkInclusion("ab", "eidbaooo"))

    def test_basic_negative(self):
        # Basic negative case (permutation does not exist)
        self.assertFalse(self.solution.checkInclusion("ab", "eidboaoo"))

    def test_equal_length_positive(self):
        # Case where s1 and s2 have equal length, and permutation exists
        self.assertTrue(self.solution.checkInclusion("abc", "bca"))

    def test_equal_length_negative(self):
        # Case where s1 and s2 have equal length, and permutation does not exist
        self.assertFalse(self.solution.checkInclusion("abc", "bcd"))

    def test_s1_length_1_positive(self):
        # Case where s1 length is 1
        self.assertTrue(self.solution.checkInclusion("a", "bac"))

    def test_s1_length_1_negative(self):
        # Case where s1 length is 1
        self.assertFalse(self.solution.checkInclusion("d", "bac"))

    def test_s1_longer_than_s2(self):
        # Case where s1 length > s2 length
        self.assertFalse(self.solution.checkInclusion("abcd", "abc"))

    def test_large_input(self):
        # Large input case near constraint limit (1000)
        s1 = "a" * 500 + "b" * 500
        s2 = "c" * 900 + "b" * 500 + "a" * 500 + "d" * 100
        self.assertTrue(self.solution.checkInclusion(s1, s2))

        s2_negative = "c" * 900 + "b" * 499 + "a" * 501 + "d" * 100
        self.assertFalse(self.solution.checkInclusion(s1, s2_negative))


if __name__ == '__main__':
    unittest.main()
