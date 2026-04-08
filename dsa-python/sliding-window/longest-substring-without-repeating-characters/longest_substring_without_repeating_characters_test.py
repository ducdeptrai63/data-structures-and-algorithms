import unittest
import string
import random

from longest_substring_without_repeating_characters import Solution


class TestLongestSubstringWithoutRepeatingCharacters(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_empty_string(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring(""), 0)

    def test_all_identical_characters(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("aaaaaa"), 1)

    def test_all_unique_characters(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcdef"), 6)

    def test_mixed_case(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(self.solution.lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(self.solution.lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(self.solution.lengthOfLongestSubstring("dvdf"), 3)

    def test_printable_ascii_characters(self):
        printable = string.printable
        expected = len(set(printable))
        self.assertEqual(
            self.solution.lengthOfLongestSubstring(printable),
            expected
        )

    def test_max_length_case(self):
        # Generate a random string of length 1000 from printable ASCII
        random_string = ''.join(random.choices(string.printable, k=1000))
        result = self.solution.lengthOfLongestSubstring(random_string)
        self.assertTrue(0 <= result <= 1000)


if __name__ == "__main__":
    unittest.main()
