import unittest

from word_break import Solution


class TestWordBreak(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_basic_true(self):
        s = "leetcode"
        word_dict = ["leet", "code"]
        self.assertTrue(self.solution.wordBreak(s, word_dict))

    def test_basic_false(self):
        s = "catsandog"
        word_dict = ["cats", "dog", "sand", "and", "cat"]
        self.assertFalse(self.solution.wordBreak(s, word_dict))

    def test_empty_string_true(self):
        s = ""
        word_dict = ["a", "abc"]
        self.assertTrue(self.solution.wordBreak(s, word_dict))

    def test_single_char_true(self):
        s = "a"
        word_dict = ["a"]
        self.assertTrue(self.solution.wordBreak(s, word_dict))

    def test_single_char_false(self):
        s = "b"
        word_dict = ["a"]
        self.assertFalse(self.solution.wordBreak(s, word_dict))

    def test_overlapping_words_true(self):
        s = "applepenapple"
        word_dict = ["apple", "pen"]
        self.assertTrue(self.solution.wordBreak(s, word_dict))

    def test_reuse_word_true(self):
        s = "aaaaaaa"
        word_dict = ["aaaa", "aaa"]
        self.assertTrue(self.solution.wordBreak(s, word_dict))

    def test_prefix_mismatch_false(self):
        s = "abcd"
        word_dict = ["ab", "abc", "cdx"]
        self.assertFalse(self.solution.wordBreak(s, word_dict))

    def test_word_dict_contains_longer_word(self):
        s = "hi"
        word_dict = ["hello", "hi"]
        self.assertTrue(self.solution.wordBreak(s, word_dict))

    def test_many_options_true(self):
        s = "catsanddog"
        word_dict = ["cats", "cat", "and", "sand", "dog"]
        self.assertTrue(self.solution.wordBreak(s, word_dict))


if __name__ == "__main__":
    unittest.main()
