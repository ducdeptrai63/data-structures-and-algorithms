import unittest

from longest_common_prefix import Solution


class TestLongestCommonPrefix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_partial_match(self):
        self.assertEqual(self.solution.longestCommonPrefix(
            ["flower", "flow", "flight"]), "fl")

    def test_full_match(self):
        self.assertEqual(self.solution.longestCommonPrefix(
            ["flower", "flower", "flower"]), "flower")

    def test_no_prefix(self):
        self.assertEqual(self.solution.longestCommonPrefix(
            ["dog", "racecar", "car"]), "")

    def test_single_string(self):
        self.assertEqual(
            self.solution.longestCommonPrefix(["flower"]), "flower")

    def test_empty_string_in_list(self):
        self.assertEqual(self.solution.longestCommonPrefix(
            ["flower", "", "flight"]), "")

    def test_all_empty_strings(self):
        self.assertEqual(self.solution.longestCommonPrefix(["", "", ""]), "")

    def test_identical_strings(self):
        self.assertEqual(self.solution.longestCommonPrefix(
            ["abc", "abc", "abc"]), "abc")

    def test_first_char_mismatch(self):
        self.assertEqual(self.solution.longestCommonPrefix(
            ["abc", "def", "ghi"]), "")

    def test_one_string_is_prefix_of_others(self):
        self.assertEqual(self.solution.longestCommonPrefix(
            ["ab", "abc", "abcd"]), "ab")

    def test_long_common_prefix_then_diverge(self):
        self.assertEqual(self.solution.longestCommonPrefix(
            ["abcdefghijk", "abcdefghijz", "abcdefghiab"]), "abcdefghi")

    def test_boundary_len_strs_1(self):
        self.assertEqual(self.solution.longestCommonPrefix(["a"]), "a")

    def test_boundary_len_strs_200(self):
        strs = ["prefix"] * 200
        self.assertEqual(self.solution.longestCommonPrefix(strs), "prefix")

    def test_boundary_len_str_0(self):
        self.assertEqual(self.solution.longestCommonPrefix([""]), "")

    def test_boundary_len_str_200(self):
        long_str = "a" * 200
        self.assertEqual(self.solution.longestCommonPrefix(
            [long_str, long_str]), long_str)
        self.assertEqual(self.solution.longestCommonPrefix(
            [long_str, "a" * 199 + "b"]), "a" * 199)


if __name__ == '__main__':
    unittest.main()
