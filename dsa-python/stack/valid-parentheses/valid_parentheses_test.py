import unittest

from valid_parentheses import Solution


class TestValidParentheses(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty_string_is_valid(self):
        self.assertTrue(self.sol.isValid(""))

    def test_single_pairs_are_valid(self):
        self.assertTrue(self.sol.isValid("()"))
        self.assertTrue(self.sol.isValid("[]"))
        self.assertTrue(self.sol.isValid("{}"))

    def test_concatenated_pairs_are_valid(self):
        self.assertTrue(self.sol.isValid("()[]{}"))
        self.assertTrue(self.sol.isValid("{}()[]"))

    def test_nested_pairs_are_valid(self):
        self.assertTrue(self.sol.isValid("{[()]}"))
        self.assertTrue(self.sol.isValid("([{}])"))
        self.assertTrue(self.sol.isValid("(((())))"))

    def test_mixed_nested_and_concatenated_valid(self):
        self.assertTrue(self.sol.isValid("{[]()}()"))
        self.assertTrue(self.sol.isValid("([]){}[()]"))

    def test_odd_length_is_invalid(self):
        self.assertFalse(self.sol.isValid("("))
        self.assertFalse(self.sol.isValid("["))
        self.assertFalse(self.sol.isValid("{"))

    def test_wrong_closing_order_is_invalid(self):
        self.assertFalse(self.sol.isValid("(]"))
        self.assertFalse(self.sol.isValid("([)]"))
        self.assertFalse(self.sol.isValid("{[}]"))

    def test_starts_with_closing_is_invalid(self):
        self.assertFalse(self.sol.isValid(")"))
        self.assertFalse(self.sol.isValid("]"))
        self.assertFalse(self.sol.isValid("}"))

    def test_leftover_opening_is_invalid(self):
        self.assertFalse(self.sol.isValid("((("))
        self.assertFalse(self.sol.isValid("{[]"))

    def test_complex_invalid_interleaving(self):
        self.assertFalse(self.sol.isValid("([]{})}"))
        self.assertFalse(self.sol.isValid("([{}]))"))


if __name__ == "__main__":
    unittest.main()
