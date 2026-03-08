import unittest

from score_of_a_string import Solution


class TestScoreOfString(unittest.TestCase):
    def test_single_character_score_zero(self):
        solution = Solution()
        self.assertEqual(solution.scoreOfString("a"), 0)

    def test_two_characters_simple_diff(self):
        solution = Solution()
        self.assertEqual(solution.scoreOfString("ab"), 1)

    def test_two_characters_reverse_diff(self):
        solution = Solution()
        self.assertEqual(solution.scoreOfString("ba"), 1)

    def test_multiple_characters_known_value(self):
        solution = Solution()
        self.assertEqual(solution.scoreOfString("hello"), 13)

    def test_mixed_case_characters(self):
        solution = Solution()
        self.assertEqual(solution.scoreOfString("aA"), 32)

    def test_repeated_characters_all_zero(self):
        solution = Solution()
        self.assertEqual(solution.scoreOfString("aaaaaa"), 0)

    def test_longer_string_varied_chars(self):
        solution = Solution()
        self.assertEqual(solution.scoreOfString("azAZ09"), 158)


if __name__ == "__main__":
    unittest.main()
