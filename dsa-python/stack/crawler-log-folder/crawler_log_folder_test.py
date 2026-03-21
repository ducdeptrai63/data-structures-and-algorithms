import unittest

from crawler_log_folder import Solution


class TestCrawlerLogFolder(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty_logs_returns_zero(self):
        self.assertEqual(self.sol.minOperations([]), 0)

    def test_only_current_dir_no_effect(self):
        self.assertEqual(self.sol.minOperations(["./", "./", "./"]), 0)

    def test_only_parent_dir_never_below_zero(self):
        self.assertEqual(self.sol.minOperations(["../", "../", "../"]), 0)

    def test_single_folder_enter_increments_depth(self):
        self.assertEqual(self.sol.minOperations(["d1/"]), 1)

    def test_folder_then_current_dir_keeps_depth(self):
        self.assertEqual(self.sol.minOperations(["d1/", "./", "./"]), 1)

    def test_folder_then_parent_dir_returns_to_zero(self):
        self.assertEqual(self.sol.minOperations(["d1/", "../"]), 0)

    def test_canonical_example_1(self):
        logs = ["d1/", "d2/", "../", "d21/", "./"]
        self.assertEqual(self.sol.minOperations(logs), 2)

    def test_canonical_example_2(self):
        logs = ["d1/", "d2/", "./", "d3/", "../", "d31/"]
        self.assertEqual(self.sol.minOperations(logs), 3)

    def test_canonical_example_3_excess_parents_at_root(self):
        logs = ["d1/", "../", "../", "../"]
        self.assertEqual(self.sol.minOperations(logs), 0)

    def test_mixed_sequence_with_multiple_returns_to_root(self):
        logs = ["a/", "b/", "c/", "../", "../", "./", "../", "../", "x/"]
        self.assertEqual(self.sol.minOperations(logs), 1)

    def test_non_special_tokens_always_increment(self):
        logs = ["folder/", "not_special/", "another/"]
        self.assertEqual(self.sol.minOperations(logs), 3)

    def test_longer_sequence_accumulates_correctly(self):
        logs = [
            "a/",
            "b/",
            "c/",
            "./",
            "../",
            "d/",
            "../",
            "../",
            "./",
            "e/",
            "f/",
            "../",
            "g/",
        ]
        self.assertEqual(self.sol.minOperations(logs), 3)


if __name__ == "__main__":
    unittest.main()
