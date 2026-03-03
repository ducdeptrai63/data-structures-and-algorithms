import unittest

from valid_palindrome import Solution


class TestValidPalindrome(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_palindrome_basic_true(self):
        self.assertTrue(self.sol.isPalindrome("racecar"))
        self.assertTrue(self.sol.isPalindrome("RaceCar"))

    def test_palindrome_basic_false(self):
        self.assertFalse(self.sol.isPalindrome("hello"))
        self.assertFalse(self.sol.isPalindrome("palindrome"))

    def test_palindrome_with_spaces_and_punctuation(self):
        self.assertTrue(self.sol.isPalindrome(
            "A man, a plan, a canal: Panama"))
        self.assertTrue(self.sol.isPalindrome("No 'x' in Nixon"))
        self.assertFalse(self.sol.isPalindrome("This, is not!"))

    def test_palindrome_with_numbers(self):
        self.assertTrue(self.sol.isPalindrome("12321"))
        self.assertTrue(self.sol.isPalindrome("12,321"))
        self.assertFalse(self.sol.isPalindrome("12345"))

    def test_palindrome_edge_cases(self):
        self.assertTrue(self.sol.isPalindrome(""))
        self.assertTrue(self.sol.isPalindrome(" "))
        self.assertTrue(self.sol.isPalindrome("!!!"))
        self.assertTrue(self.sol.isPalindrome("a"))
        self.assertTrue(self.sol.isPalindrome("Aa"))

    def test_palindrome_mixed_alnum_and_symbols(self):
        self.assertTrue(self.sol.isPalindrome("ab@#ba"))
        self.assertFalse(self.sol.isPalindrome("ab@#ca"))
        self.assertFalse(self.sol.isPalindrome("0P"))


if __name__ == "__main__":
    unittest.main()
