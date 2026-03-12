import unittest

from take_gifts_from_the_richest_pile import Solution


class TestTakeGiftsFromTheRichestPile(unittest.TestCase):
    def test_basic_small_case(self):
        sol = Solution()
        self.assertEqual(sol.pickGifts([25, 64, 9, 4, 100], 4), 29)

    def test_k_zero_no_change(self):
        sol = Solution()
        self.assertEqual(sol.pickGifts([10, 20, 30], 0), 60)

    def test_single_pile_multiple_operations(self):
        sol = Solution()
        self.assertEqual(sol.pickGifts([81], 3), 1)

    def test_k_greater_than_len(self):
        sol = Solution()
        self.assertEqual(sol.pickGifts([8, 1], 5), 2)

    def test_all_ones_stable(self):
        sol = Solution()
        self.assertEqual(sol.pickGifts([1, 1, 1, 1], 10), 4)

    def test_perfect_squares(self):
        sol = Solution()
        self.assertEqual(sol.pickGifts([16, 9, 4], 2), 11)

    def test_mixed_values(self):
        sol = Solution()
        self.assertEqual(sol.pickGifts([7, 2, 3, 9], 3), 8)

    def test_large_k_converges_to_ones(self):
        sol = Solution()
        self.assertEqual(sol.pickGifts([100, 100, 100], 10), 3)


if __name__ == "__main__":
    unittest.main()
