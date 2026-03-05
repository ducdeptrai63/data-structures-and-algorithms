import unittest

from palindromic_substrings import Solution


class TestPalindromicSubstrings(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty_string(self):
        self.assertEqual(self.sol.countSubstrings(""), 0)

    def test_single_character(self):
        self.assertEqual(self.sol.countSubstrings("a"), 1)

    def test_two_different_characters(self):
        self.assertEqual(self.sol.countSubstrings("ab"), 2)

    def test_two_same_characters(self):
        self.assertEqual(self.sol.countSubstrings("aa"), 3)

    def test_example_aaa(self):
        self.assertEqual(self.sol.countSubstrings("aaa"), 6)

    def test_example_abc(self):
        self.assertEqual(self.sol.countSubstrings("abc"), 3)

    def test_example_aba(self):
        self.assertEqual(self.sol.countSubstrings("aba"), 4)

    def test_example_abba(self):
        self.assertEqual(self.sol.countSubstrings("abba"), 6)

    def test_mixed_pattern(self):
        self.assertEqual(self.sol.countSubstrings("abac"), 5)

    def test_all_same_large(self):
        n = 5
        s = "a" * n
        self.assertEqual(self.sol.countSubstrings(s), n * (n + 1) // 2)

    def test_palindromic_center(self):
        self.assertEqual(self.sol.countSubstrings("racecar"), 10)


if __name__ == "__main__":
    unittest.main()
