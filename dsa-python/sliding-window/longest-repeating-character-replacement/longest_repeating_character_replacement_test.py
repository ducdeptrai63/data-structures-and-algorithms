import unittest

from longest_repeating_character_replacement import Solution


class TestLongestRepeatingCharacterReplacement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minimum_length_string(self):
        """Test with minimum string length constraints (s.length = 1)"""
        self.assertEqual(self.solution.characterReplacement("A", 0), 1)
        self.assertEqual(self.solution.characterReplacement("A", 1), 1)

    def test_k_is_zero(self):
        """Test scenarios where no replacements are allowed (k = 0)"""
        self.assertEqual(self.solution.characterReplacement("AABABBA", 0), 2)
        self.assertEqual(self.solution.characterReplacement("ABCDE", 0), 1)
        self.assertEqual(self.solution.characterReplacement("AAAA", 0), 4)

    def test_k_is_s_length(self):
        """Test scenarios where k is equal to the length of string s"""
        self.assertEqual(self.solution.characterReplacement("ABCDEF", 6), 6)
        self.assertEqual(self.solution.characterReplacement("XYZ", 3), 3)

    def test_all_identical_characters(self):
        """Test strings containing all identical characters"""
        self.assertEqual(self.solution.characterReplacement("AAAA", 1), 4)
        self.assertEqual(self.solution.characterReplacement("BBBBB", 0), 5)
        self.assertEqual(self.solution.characterReplacement("CCCCC", 5), 5)

    def test_all_distinct_characters(self):
        """Test strings containing all distinct characters"""
        self.assertEqual(self.solution.characterReplacement("ABCDEFGH", 3), 4)
        self.assertEqual(self.solution.characterReplacement("XYZ", 1), 2)

    def test_large_input_near_upper_bound(self):
        """Test with large inputs near the upper bound constraint of 1000"""
        # Test case: 500 'A's followed by 500 'B's, k = 500
        s1 = "A" * 500 + "B" * 500
        self.assertEqual(self.solution.characterReplacement(s1, 500), 1000)
        self.assertEqual(self.solution.characterReplacement(s1, 0), 500)

        # Test case: 1 'C' followed by 999 'D's, k = 1
        s2 = "C" + "D" * 999
        self.assertEqual(self.solution.characterReplacement(s2, 1), 1000)

    def test_typical_cases(self):
        """Test typical use cases provided as examples"""
        self.assertEqual(self.solution.characterReplacement("ABAB", 2), 4)
        self.assertEqual(self.solution.characterReplacement("AABABBA", 1), 4)


if __name__ == '__main__':
    unittest.main()
