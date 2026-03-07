import unittest

from last_stone_weight import Solution


class TestLastStoneWeight(unittest.TestCase):
    def test_example_case(self):
        stones = [2, 7, 4, 1, 8, 1]
        result = Solution().lastStoneWeight(stones.copy())
        self.assertEqual(result, 1)

    def test_all_equal(self):
        stones = [5, 5, 5, 5]
        result = Solution().lastStoneWeight(stones.copy())
        self.assertEqual(result, 0)

    def test_single_stone(self):
        stones = [9]
        result = Solution().lastStoneWeight(stones.copy())
        self.assertEqual(result, 9)

    def test_empty_list(self):
        stones = []
        result = Solution().lastStoneWeight(stones.copy())
        self.assertEqual(result, 0)

    def test_two_equal_stones(self):
        stones = [3, 3]
        result = Solution().lastStoneWeight(stones.copy())
        self.assertEqual(result, 0)

    def test_two_unequal_stones(self):
        stones = [10, 3]
        result = Solution().lastStoneWeight(stones.copy())
        self.assertEqual(result, 7)

    def test_order_independence(self):
        stones = [1, 3, 3, 7]
        result = Solution().lastStoneWeight(stones.copy())
        self.assertEqual(result, 0)

    def test_larger_case(self):
        stones = [31, 26, 33, 21, 40]
        result = Solution().lastStoneWeight(stones.copy())
        self.assertEqual(result, 9)


if __name__ == "__main__":
    unittest.main()
