import unittest

from number_of_islands import Solution


class TestNumberOfIslands(unittest.TestCase):
    def test_single_cell_land(self):
        grid = [["1"]]
        result = Solution().numIslands(grid)
        self.assertEqual(result, 1)

    def test_single_cell_water(self):
        grid = [["0"]]
        result = Solution().numIslands(grid)
        self.assertEqual(result, 0)

    def test_all_land_rectangle(self):
        grid = [
            ["1", "1", "1"],
            ["1", "1", "1"],
        ]
        result = Solution().numIslands(grid)
        self.assertEqual(result, 1)

    def test_all_water_rectangle(self):
        grid = [
            ["0", "0", "0"],
            ["0", "0", "0"],
        ]
        result = Solution().numIslands(grid)
        self.assertEqual(result, 0)

    def test_multiple_separated(self):
        grid = [
            ["1", "0", "1", "0"],
            ["0", "0", "0", "1"],
            ["1", "0", "1", "1"],
            ["0", "0", "0", "0"],
        ]
        result = Solution().numIslands(grid)
        self.assertEqual(result, 4)

    def test_diagonal_not_connected(self):
        grid = [
            ["1", "0", "0"],
            ["0", "1", "0"],
            ["0", "0", "1"],
        ]
        result = Solution().numIslands(grid)
        self.assertEqual(result, 3)

    def test_long_row(self):
        grid = [["1", "1", "0", "1", "0", "1", "1", "1"]]
        result = Solution().numIslands(grid)
        self.assertEqual(result, 3)

    def test_long_column(self):
        grid = [
            ["1"],
            ["0"],
            ["1"],
            ["1"],
            ["0"],
            ["1"],
        ]
        result = Solution().numIslands(grid)
        self.assertEqual(result, 3)

    def test_complex_shape(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        result = Solution().numIslands(grid)
        self.assertEqual(result, 3)

    def test_three_islands_case(self):
        grid = [
            ["1", "0", "1"],
            ["1", "1", "0"],
            ["0", "0", "1"],
        ]
        result = Solution().numIslands(grid)
        self.assertEqual(result, 3)

    def test_large_mixed(self):
        grid = [
            ["1", "0", "1", "1", "0", "0"],
            ["1", "0", "0", "1", "0", "1"],
            ["0", "0", "1", "0", "0", "1"],
            ["1", "1", "0", "0", "1", "0"],
            ["0", "1", "0", "1", "1", "0"],
        ]
        result = Solution().numIslands(grid)
        self.assertEqual(result, 6)


if __name__ == "__main__":
    unittest.main()
