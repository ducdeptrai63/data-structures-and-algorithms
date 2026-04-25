import unittest

from valid_palindrome_2 import Solution


class TestValidPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_already_palindrome(self):
        self.assertTrue(self.solution.validPalindrome("aba"))
        self.assertTrue(self.solution.validPalindrome("racecar"))

    def test_delete_one_char_makes_palindrome(self):
        self.assertTrue(self.solution.validPalindrome("abca"))
        self.assertFalse(self.solution.validPalindrome("abecbea"))
        self.assertTrue(self.solution.validPalindrome("caba"))
        self.assertTrue(self.solution.validPalindrome("abac"))

    def test_impossible_case(self):
        self.assertFalse(self.solution.validPalindrome("abc"))
        self.assertFalse(self.solution.validPalindrome("abdecbea"))

    def test_length_1(self):
        self.assertTrue(self.solution.validPalindrome("a"))

    def test_length_2(self):
        self.assertTrue(self.solution.validPalindrome("ab"))
        self.assertTrue(self.solution.validPalindrome("aa"))

    def test_all_same_characters(self):
        self.assertTrue(self.solution.validPalindrome("aaaaa"))

    def test_large_input_palindrome(self):
        s = "a" * 100000
        self.assertTrue(self.solution.validPalindrome(s))

    def test_large_input_almost_palindrome_left(self):
        s = "b" + "a" * 99999
        self.assertTrue(self.solution.validPalindrome(s))

    def test_large_input_almost_palindrome_right(self):
        s = "a" * 99999 + "b"
        self.assertTrue(self.solution.validPalindrome(s))

    def test_large_input_almost_palindrome_middle(self):
        s = "a" * 50000 + "b" + "a" * 49999
        self.assertTrue(self.solution.validPalindrome(s))

    def test_large_input_impossible(self):
        s = "b" + "a" * 99998 + "c"
        self.assertFalse(self.solution.validPalindrome(s))


if __name__ == '__main__':
    unittest.main()
