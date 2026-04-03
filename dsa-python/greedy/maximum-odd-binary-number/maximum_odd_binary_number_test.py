import unittest

from maximum_odd_binary_number import Solution


class TestMaximumOddBinaryNumber(unittest.TestCase):
    def setUp(self) -> None:
        self.sln = Solution()

    @staticmethod
    def _expected_maximum_odd_binary_number(s: str) -> str:
        ones = s.count("1")
        n = len(s)
        # Lexicographically largest odd binary string with the same number of 1s:
        # put (ones-1) ones first, then all zeros, and ensure last char is '1'.
        return "1" * (ones - 1) + "0" * (n - ones) + "1"

    @staticmethod
    def _bruteforce_maximum_odd_binary_number(s: str) -> str:
        n = len(s)
        ones = s.count("1")
        best = None

        # Enumerate all binary strings of length n with exactly `ones` ones.
        # Keep only odd candidates (ending in '1') and track the lexicographic max.
        for mask in range(1 << n):
            if mask.bit_count() != ones:
                continue

            candidate = "".join(
                "1" if (mask & (1 << (n - 1 - i))) else "0" for i in range(n)
            )
            if candidate[-1] != "1":
                continue

            if best is None or candidate > best:
                best = candidate

        # Constraint guarantees at least one '1', so an odd candidate always exists.
        return best  # type: ignore[return-value]

    def _assert_valid(self, s: str):
        out = self.sln.maximumOddBinaryNumber(s)
        expected = self._expected_maximum_odd_binary_number(s)

        self.assertEqual(len(out), len(s))
        self.assertEqual(out.count("1"), s.count("1"))
        self.assertTrue(out.endswith("1"))
        self.assertEqual(out, expected)

        # For small n, additionally prove maximality via brute force.
        if len(s) <= 12:
            self.assertEqual(
                out, self._bruteforce_maximum_odd_binary_number(s))

    # A. Minimum length case
    def test_min_length_one(self):
        self._assert_valid("1")

    # B. Small strings
    def test_small_strings(self):
        for s in ["10", "01", "11"]:
            self._assert_valid(s)

    # C. Typical mixed cases
    def test_typical_mixed_balanced(self):
        # Balanced zeros/ones.
        self._assert_valid("0101")  # 2 ones, 2 zeros
        self._assert_valid("0011")  # 2 ones, 2 zeros

    def test_typical_more_zeros_than_ones(self):
        self._assert_valid("0001000")  # 1 one, 6 zeros
        self._assert_valid("010000")  # 1 one, 5 zeros

    def test_typical_more_ones_than_zeros(self):
        self._assert_valid("111010")  # 4 ones, 2 zeros
        self._assert_valid("1101110")  # 5 ones, 2 zeros

    # D. Edge cases
    def test_edge_only_one_one_rest_zeros(self):
        self._assert_valid("1000")
        self._assert_valid("0000001")

    def test_edge_all_ones(self):
        self._assert_valid("1")
        self._assert_valid("1111")
        self._assert_valid("1" * 99)

    def test_edge_long_near_100(self):
        s = ("01" * 50)  # length 100, 50 ones
        self.assertEqual(len(s), 100)
        self.assertEqual(s.count("1"), 50)
        self._assert_valid(s)

    def test_edge_random_distribution(self):
        # Deterministic pseudo-random-looking distribution.
        s = "10100101101001011001"  # length 20
        self.assertEqual(len(s), 20)
        self.assertGreaterEqual(s.count("1"), 1)
        self._assert_valid(s)

    # E. Already maximum odd binary arrangement
    def test_already_maximum_odd_binary_arrangement(self):
        s = "1110001"  # already of the form 1...(zeros)...1
        self.assertEqual(s, self._expected_maximum_odd_binary_number(s))
        self._assert_valid(s)

    # F. Completely unsorted input
    def test_completely_unsorted_input(self):
        s = "01010101010000100101"
        self._assert_valid(s)


if __name__ == "__main__":
    unittest.main()
