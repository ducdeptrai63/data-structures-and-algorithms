import unittest

from verifying_an_alien_dictionary import Solution


class TestVerifyingAlienDictionary(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_basic_valid_ordering(self):
        words = ["hello", "leetcode"]
        order = "hlabcdefgijkmnopqrstuvwxyz"
        self.assertTrue(self.s.isAlienSorted(words, order))

    def test_basic_invalid_ordering(self):
        words = ["word", "world", "row"]
        order = "worldabcefghijkmnpqstuvxyz"
        self.assertFalse(self.s.isAlienSorted(words, order))

    def test_prefix_invalid_when_longer_first(self):
        words = ["apple", "app"]
        order = "abcdefghijklmnopqrstuvwxyz"
        self.assertFalse(self.s.isAlienSorted(words, order))

    def test_prefix_valid_when_shorter_first(self):
        words = ["app", "apple"]
        order = "abcdefghijklmnopqrstuvwxyz"
        self.assertTrue(self.s.isAlienSorted(words, order))

    def test_identical_words_valid(self):
        words = ["same", "same", "same"]
        order = "abcdefghijklmnopqrstuvwxyz"
        self.assertTrue(self.s.isAlienSorted(words, order))

    def test_single_word_valid(self):
        words = ["solo"]
        order = "abcdefghijklmnopqrstuvwxyz"
        self.assertTrue(self.s.isAlienSorted(words, order))

    def test_mismatch_late_character_valid(self):
        words = ["aaab", "aaac"]
        order = "abcdefghijklmnopqrstuvwxyz"
        self.assertTrue(self.s.isAlienSorted(words, order))

    def test_mismatch_late_character_invalid(self):
        words = ["aaac", "aaab"]
        order = "abcdefghijklmnopqrstuvwxyz"
        self.assertFalse(self.s.isAlienSorted(words, order))

    def test_custom_order_all_sorted(self):
        words = ["xww", "wxyz", "wxyw", "ywx", "ywz"]
        order = "xwyzabcdefghijklmnopqrstuv"
        self.assertFalse(self.s.isAlienSorted(words, order))


if __name__ == "__main__":
    unittest.main()
