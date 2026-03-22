import itertools
import unittest

from minimum_recolors_to_get_k_consecutive_black_blocks import Solution


class TestMinimumRecolorsToGetKConsecutiveBlackBlocks(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def _bruteforce(self, blocks: str, k: int) -> int:
        best = None
        for i in range(0, len(blocks) - k + 1):
            recolors = blocks[i: i + k].count("W")
            best = recolors if best is None else min(best, recolors)
        return 0 if best is None else best

    def testSingleCharacterK1BlackIsZero(self):
        self.assertEqual(self.solution.minimumRecolors("B", 1), 0)

    def testSingleCharacterK1WhiteIsOne(self):
        self.assertEqual(self.solution.minimumRecolors("W", 1), 1)

    def testKEqualsLengthCountsAllWhites(self):
        blocks = "BWBWW"
        k = len(blocks)
        self.assertEqual(self.solution.minimumRecolors(
            blocks, k), blocks.count("W"))

    def testAllBlackMultipleKAlwaysZero(self):
        blocks = "BBBBBB"
        self.assertEqual(self.solution.minimumRecolors(blocks, 1), 0)
        self.assertEqual(self.solution.minimumRecolors(blocks, 3), 0)
        self.assertEqual(self.solution.minimumRecolors(blocks, 6), 0)

    def testAllWhiteResultEqualsK(self):
        blocks = "WWWWW"
        self.assertEqual(self.solution.minimumRecolors(blocks, 1), 1)
        self.assertEqual(self.solution.minimumRecolors(blocks, 3), 3)
        self.assertEqual(self.solution.minimumRecolors(blocks, 5), 5)

    def testKnownCaseRequiresThreeRecolors(self):
        self.assertEqual(self.solution.minimumRecolors("WBBWWBBWBW", 7), 3)

    def testKnownCaseAlreadyHasConsecutiveBlacks(self):
        self.assertEqual(self.solution.minimumRecolors("WBWBBBW", 2), 0)

    def testSlidingWindowMovesCorrectly(self):
        # k=3 windows:
        # BWW -> 2, WWB -> 2, WBB -> 1, BBB -> 0, BBW -> 1 => min 0
        self.assertEqual(self.solution.minimumRecolors("BWWBBBW", 3), 0)

    def testMatchesBruteforceForAllSmallStrings(self):
        for n in range(1, 8):
            for tup in itertools.product("BW", repeat=n):
                blocks = "".join(tup)
                for k in range(1, n + 1):
                    expected = self._bruteforce(blocks, k)
                    actual = self.solution.minimumRecolors(blocks, k)
                    self.assertEqual(
                        actual,
                        expected,
                        msg=f"blocks={blocks!r}, k={k}",
                    )


if __name__ == "__main__":
    unittest.main()
