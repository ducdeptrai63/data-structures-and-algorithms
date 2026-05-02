import unittest

from append_characters_to_string_to_make_subsequence import Solution


class TestAppendCharactersToStringToMakeSubsequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minimum_length_match(self):
        self.assertEqual(self.solution.appendCharacters("a", "a"), 0)

    def test_minimum_length_no_match(self):
        self.assertEqual(self.solution.appendCharacters("a", "b"), 1)

    def test_already_subsequence(self):
        self.assertEqual(self.solution.appendCharacters("abcde", "ace"), 0)
        self.assertEqual(self.solution.appendCharacters("z", "z"), 0)
        self.assertEqual(self.solution.appendCharacters("abcdef", "a"), 0)

    def test_no_common_characters(self):
        self.assertEqual(self.solution.appendCharacters("abc", "xyz"), 3)
        self.assertEqual(self.solution.appendCharacters("aaaa", "bbbb"), 4)

    def test_typical_cases(self):
        self.assertEqual(self.solution.appendCharacters(
            "coaching", "coding"), 4)
        self.assertEqual(self.solution.appendCharacters("abcde", "a"), 0)
        self.assertEqual(self.solution.appendCharacters("z", "abcde"), 5)

    def test_large_input_already_subsequence(self):
        s = "a" * 100000
        t = "a" * 100000
        self.assertEqual(self.solution.appendCharacters(s, t), 0)

    def test_large_input_no_common_characters(self):
        s = "a" * 100000
        t = "b" * 100000
        self.assertEqual(self.solution.appendCharacters(s, t), 100000)

    def test_large_input_partial_match(self):
        s = "a" * 50000 + "b" * 50000
        t = "a" * 100000
        self.assertEqual(self.solution.appendCharacters(s, t), 50000)

        s2 = "ab" * 50000
        t2 = "a" * 50000
        self.assertEqual(self.solution.appendCharacters(s2, t2), 0)


if __name__ == '__main__':
    unittest.main()
