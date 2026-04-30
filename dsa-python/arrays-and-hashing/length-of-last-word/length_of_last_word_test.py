import unittest

from length_of_last_word import Solution


class TestLengthOfLastWord(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_word(self):
        self.assertEqual(self.solution.lengthOfLastWord("Hello"), 5)

    def test_multiple_words(self):
        self.assertEqual(self.solution.lengthOfLastWord("Hello World"), 5)

    def test_trailing_spaces(self):
        self.assertEqual(self.solution.lengthOfLastWord(
            "   fly me   to   the moon  "), 4)

    def test_multiple_spaces_between_words(self):
        self.assertEqual(self.solution.lengthOfLastWord(
            "luffy is still joyboy"), 6)

    def test_single_letter(self):
        self.assertEqual(self.solution.lengthOfLastWord("a"), 1)

    def test_single_letter_with_spaces(self):
        self.assertEqual(self.solution.lengthOfLastWord(" a "), 1)

    def test_leading_spaces_only(self):
        self.assertEqual(self.solution.lengthOfLastWord("      word"), 4)

    def test_max_length_input(self):
        # 10000 length string with a single word at the end
        s1 = "a" * 9999 + " b"
        self.assertEqual(self.solution.lengthOfLastWord(s1), 1)

        # Max length with multiple words
        s2 = "word " * 1998 + "lastword"  # approx 10000 chars
        self.assertEqual(self.solution.lengthOfLastWord(s2), 8)

        # Max length with only spaces and one word
        s3 = " " * 9996 + "word"
        self.assertEqual(self.solution.lengthOfLastWord(s3), 4)

        # Max length with word at the beginning and trailing spaces
        s4 = "word" + " " * 9996
        self.assertEqual(self.solution.lengthOfLastWord(s4), 4)

        # Exact max length of 10000 characters of a single word
        s5 = "a" * 10000
        self.assertEqual(self.solution.lengthOfLastWord(s5), 10000)


if __name__ == '__main__':
    unittest.main()
