import unittest

from verifying_an_alien_dictionary import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_typical_case_true(self):
        words = ["hello", "leetcode"]
        order = "hlabcdefgijkmnopqrstuvwxyz"
        self.assertTrue(self.solution.isAlienSorted(words, order))

    def test_typical_case_false(self):
        words = ["word", "world", "row"]
        order = "worldabcefghijkmnpqstuvxyz"
        self.assertFalse(self.solution.isAlienSorted(words, order))

    def test_prefix_false(self):
        words = ["apple", "app"]
        order = "abcdefghijklmnopqrstuvwxyz"
        self.assertFalse(self.solution.isAlienSorted(words, order))

    def test_prefix_true(self):
        words = ["app", "apple"]
        order = "abcdefghijklmnopqrstuvwxyz"
        self.assertTrue(self.solution.isAlienSorted(words, order))

    def test_single_word(self):
        words = ["hello"]
        order = "abcdefghijklmnopqrstuvwxyz"
        self.assertTrue(self.solution.isAlienSorted(words, order))

    def test_all_same_words(self):
        words = ["hello", "hello", "hello"]
        order = "abcdefghijklmnopqrstuvwxyz"
        self.assertTrue(self.solution.isAlienSorted(words, order))

    def test_single_letters_true(self):
        words = ["z", "a"]
        order = "zabcdefghijklmnopqrstuvwxy"
        self.assertTrue(self.solution.isAlienSorted(words, order))

    def test_single_letters_false(self):
        words = ["a", "z"]
        order = "zabcdefghijklmnopqrstuvwxy"
        self.assertFalse(self.solution.isAlienSorted(words, order))

    def test_max_length_words(self):
        words = ["a" * 20, "a" * 19 + "b"]
        order = "abcdefghijklmnopqrstuvwxyz"
        self.assertTrue(self.solution.isAlienSorted(words, order))

    def test_large_number_of_unsorted_words(self):
        # 100 words (unsorted due to repeats)
        words = ["a", "b", "c"] * 33 + ["d"]
        order = "abcdefghijklmnopqrstuvwxyz"
        self.assertFalse(self.solution.isAlienSorted(words, order))

    def test_large_number_of_sorted_words(self):
        words = ["a", "aa", "aaa", "aaaa", "b", "bb", "c", "cc", "d"]
        order = "abcdefghijklmnopqrstuvwxyz"
        self.assertTrue(self.solution.isAlienSorted(words, order))


if __name__ == '__main__':
    unittest.main()
