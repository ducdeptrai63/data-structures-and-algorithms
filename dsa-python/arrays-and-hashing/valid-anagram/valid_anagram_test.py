import unittest

from valid_anagram import Solution


class TestValidAnagram(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_anagram(self):
        self.assertTrue(self.solution.isAnagram("anagram", "nagaram"))

    def test_basic_not_anagram(self):
        self.assertFalse(self.solution.isAnagram("rat", "car"))

    def test_different_lengths(self):
        self.assertFalse(self.solution.isAnagram("a", "ab"))

    def test_identical_strings(self):
        self.assertTrue(self.solution.isAnagram("listen", "listen"))

    def test_empty_strings(self):
        self.assertTrue(self.solution.isAnagram("", ""))

    def test_repeated_characters_anagram(self):
        self.assertTrue(self.solution.isAnagram("aabbcc", "baccab"))

    def test_repeated_characters_not_anagram(self):
        self.assertFalse(self.solution.isAnagram("aabbcc", "aabbcd"))

    def test_single_character(self):
        self.assertTrue(self.solution.isAnagram("z", "z"))

    def test_mixed_order(self):
        self.assertTrue(self.solution.isAnagram("abcabc", "cbacba"))


if __name__ == "__main__":
    unittest.main()
