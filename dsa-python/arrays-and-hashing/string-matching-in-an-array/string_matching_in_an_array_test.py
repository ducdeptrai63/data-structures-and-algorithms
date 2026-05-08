import unittest

from string_matching_in_an_array import Solution


class TestStringMatching(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minimum_input(self):
        # 1 word
        words = ["hello"]
        self.assertEqual(
            sorted(self.solution.stringMatching(words)), sorted([]))

    def test_no_substring_match(self):
        words = ["apple", "banana", "cherry"]
        self.assertEqual(
            sorted(self.solution.stringMatching(words)), sorted([]))

    def test_single_match(self):
        words = ["mass", "as", "hero", "super"]
        self.assertEqual(
            sorted(self.solution.stringMatching(words)), sorted(["as"]))

    def test_multiple_matches(self):
        words = ["mass", "as", "hero", "superhero"]
        self.assertEqual(
            sorted(self.solution.stringMatching(words)), sorted(["as", "hero"]))

    def test_all_words_are_substrings_of_others(self):
        # All words except the longest are substrings of another word
        words = ["a", "ab", "abc", "abcd"]
        self.assertEqual(sorted(self.solution.stringMatching(
            words)), sorted(["a", "ab", "abc"]))

    def test_edge_length_case(self):
        # word length = 30
        word1 = "a" * 30
        word2 = "b" * 30
        word3 = "a" * 29
        word4 = "c" * 30
        words = [word1, word2, word3, word4]
        self.assertEqual(
            sorted(self.solution.stringMatching(words)), sorted([word3]))

    def test_mixed_size_input(self):
        # near 100 words (100 words exactly)
        words = []
        for length in range(10, 14):
            for i in range(25):
                words.append(chr(97 + i) * length)

        # Words of length 10, 11, 12 will be substrings of words of length 13.
        expected = []
        for length in range(10, 13):
            for i in range(25):
                expected.append(chr(97 + i) * length)

        self.assertEqual(
            sorted(self.solution.stringMatching(words)), sorted(expected))


if __name__ == '__main__':
    unittest.main()
