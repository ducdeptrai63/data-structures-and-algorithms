import unittest

from group_anagrams import Solution


class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def assertGroupAnagramsEqual(self, actual, expected):
        """
        Helper method to compare two list of list of strings in an order-independent way.
        It sorts the elements within each group, and then sorts the outer list of groups.
        """
        def normalize(groups):
            return sorted([tuple(sorted(group)) for group in groups])

        self.assertEqual(normalize(actual), normalize(expected))

    def test_minimum_input_single_element(self):
        strs = ["a"]
        expected = [["a"]]
        self.assertGroupAnagramsEqual(
            self.solution.groupAnagrams(strs), expected)

    def test_empty_string_element(self):
        strs = [""]
        expected = [[""]]
        self.assertGroupAnagramsEqual(
            self.solution.groupAnagrams(strs), expected)

    def test_multiple_empty_strings(self):
        strs = ["", "", "a"]
        expected = [["", ""], ["a"]]
        self.assertGroupAnagramsEqual(
            self.solution.groupAnagrams(strs), expected)

    def test_duplicates(self):
        strs = ["eat", "eat", "eat"]
        expected = [["eat", "eat", "eat"]]
        self.assertGroupAnagramsEqual(
            self.solution.groupAnagrams(strs), expected)

    def test_no_anagrams(self):
        strs = ["a", "b", "c"]
        expected = [["a"], ["b"], ["c"]]
        self.assertGroupAnagramsEqual(
            self.solution.groupAnagrams(strs), expected)

    def test_all_anagrams(self):
        strs = ["abc", "cba", "bac", "cab", "bca", "acb"]
        expected = [["abc", "cba", "bac", "cab", "bca", "acb"]]
        self.assertGroupAnagramsEqual(
            self.solution.groupAnagrams(strs), expected)

    def test_mixed_groups(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        self.assertGroupAnagramsEqual(
            self.solution.groupAnagrams(strs), expected)

    def test_large_input_size(self):
        # Constraints: 1 <= strs.length <= 1000, 0 <= strs[i].length <= 100
        # Creating a large input with 1000 items of up to 100 length each.
        s1 = "a" * 50 + "b" * 50  # length 100
        s2 = "b" * 50 + "a" * 50  # anagram of s1, length 100
        s3 = "c" * 100  # different anagram group, length 100

        # 500 strings of s1/s2 group, 500 strings of s3
        strs = [s1] * 250 + [s2] * 250 + [s3] * 500

        # Expected is two groups
        expected = [[s1] * 250 + [s2] * 250, [s3] * 500]

        self.assertGroupAnagramsEqual(
            self.solution.groupAnagrams(strs), expected)


if __name__ == '__main__':
    unittest.main()
