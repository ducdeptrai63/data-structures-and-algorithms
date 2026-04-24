import unittest

from is_subsequence import Solution


class TestIsSubsequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_both_empty(self):
        self.assertTrue(self.solution.isSubsequence("", ""))

    def test_s_empty_t_non_empty(self):
        self.assertTrue(self.solution.isSubsequence("", "abc"))

    def test_t_empty_s_non_empty(self):
        self.assertFalse(self.solution.isSubsequence("abc", ""))

    def test_s_is_valid_subsequence(self):
        self.assertTrue(self.solution.isSubsequence("abc", "ahbgdc"))
        self.assertTrue(self.solution.isSubsequence("ace", "abcde"))

    def test_s_is_not_subsequence(self):
        self.assertFalse(self.solution.isSubsequence("axc", "ahbgdc"))
        self.assertFalse(self.solution.isSubsequence("aec", "abcde"))

    def test_s_equals_t(self):
        self.assertTrue(self.solution.isSubsequence("abc", "abc"))

    def test_s_longer_than_t(self):
        self.assertFalse(self.solution.isSubsequence("abcd", "abc"))

    def test_large_input(self):
        t = "a" * 9999 + "b"
        self.assertTrue(self.solution.isSubsequence("ab", t))
        self.assertTrue(self.solution.isSubsequence("a", t))
        self.assertTrue(self.solution.isSubsequence("b", t))
        self.assertFalse(self.solution.isSubsequence("c", t))
        self.assertFalse(self.solution.isSubsequence("ba", t))

    def test_typical_edge_cases(self):
        # Characters exist but frequency doesn't match
        self.assertTrue(self.solution.isSubsequence("b", "abc"))
        self.assertFalse(self.solution.isSubsequence("bb", "abc"))

        # Order matters
        self.assertFalse(self.solution.isSubsequence("cba", "abc"))

        # s matches the last character
        self.assertTrue(self.solution.isSubsequence("z", "abcz"))

        # Scattered matches
        self.assertTrue(self.solution.isSubsequence("aza", "abzczda"))


if __name__ == '__main__':
    unittest.main()
