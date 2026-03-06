import unittest

from decode_ways import Solution


class TestDecodeWays(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty_string(self):
        self.assertEqual(self.sol.numDecodings(""), 1)

    def test_single_digit_valid(self):
        self.assertEqual(self.sol.numDecodings("1"), 1)
        self.assertEqual(self.sol.numDecodings("9"), 1)

    def test_single_digit_invalid(self):
        self.assertEqual(self.sol.numDecodings("0"), 0)

    def test_leading_zero(self):
        self.assertEqual(self.sol.numDecodings("01"), 0)

    def test_simple_pairs(self):
        self.assertEqual(self.sol.numDecodings("12"), 2)
        self.assertEqual(self.sol.numDecodings("26"), 2)
        self.assertEqual(self.sol.numDecodings("27"), 1)

    def test_mixed_zeros(self):
        self.assertEqual(self.sol.numDecodings("10"), 1)
        self.assertEqual(self.sol.numDecodings("20"), 1)
        self.assertEqual(self.sol.numDecodings("100"), 0)
        self.assertEqual(self.sol.numDecodings("101"), 1)
        self.assertEqual(self.sol.numDecodings("110"), 1)
        self.assertEqual(self.sol.numDecodings("1010"), 1)

    def test_known_example(self):
        self.assertEqual(self.sol.numDecodings("226"), 3)

    def test_larger_example(self):
        self.assertEqual(self.sol.numDecodings("11106"), 2)

    def test_long_uniform(self):
        self.assertEqual(self.sol.numDecodings("111111"), 13)


if __name__ == "__main__":
    unittest.main()
