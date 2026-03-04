import unittest

from longest_palindromic_substring import Solution


class TestLongestPalindromicSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def assert_palindrome(self, s):
        self.assertEqual(s, s[::-1], "Result should be a palindrome.")

    def assert_substring(self, s, sub):
        self.assertIn(sub, s, "Result should be a substring of the input.")

    def test_empty_string(self):
        result = self.solution.longestPalindrome("")
        self.assertEqual(result, "")

    def test_single_character(self):
        result = self.solution.longestPalindrome("a")
        self.assertEqual(result, "a")

    def test_even_length_palindrome(self):
        result = self.solution.longestPalindrome("cbbd")
        self.assertEqual(result, "bb")

    def test_odd_length_palindrome_multiple_answers(self):
        result = self.solution.longestPalindrome("babad")
        self.assertIn(result, {"bab", "aba"})

    def test_all_same_characters(self):
        result = self.solution.longestPalindrome("aaaa")
        self.assertEqual(result, "aaaa")

    def test_no_longer_than_one(self):
        s = "ab"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(len(result), 1)
        self.assert_substring(s, result)
        self.assert_palindrome(result)

    def test_longer_known_palindrome(self):
        s = "forgeeksskeegfor"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, "geeksskeeg")
        self.assert_substring(s, result)
        self.assert_palindrome(result)

    def test_generic_validity(self):
        s = "abacdfgdcaba"
        result = self.solution.longestPalindrome(s)
        self.assert_substring(s, result)
        self.assert_palindrome(result)


if __name__ == "__main__":
    unittest.main()
