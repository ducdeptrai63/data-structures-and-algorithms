import unittest

from island_perimeter import Solution


class TestIslandPerimeter(unittest.TestCase):
	def setUp(self):
		self.sol = Solution()

	def test_single_cell(self):
		grid = [[1]]
		self.assertEqual(self.sol.islandPerimeter(grid), 4)

	def test_single_row_island(self):
		grid = [[1, 1, 1]]
		self.assertEqual(self.sol.islandPerimeter(grid), 8)

	def test_single_column_island(self):
		grid = [[1], [1], [1]]
		self.assertEqual(self.sol.islandPerimeter(grid), 8)

	def test_two_by_two_square(self):
		grid = [
			[1, 1],
			[1, 1],
		]
		self.assertEqual(self.sol.islandPerimeter(grid), 8)

	def test_rectangle_2x3(self):
		grid = [
			[1, 1, 1],
			[1, 1, 1],
		]
		self.assertEqual(self.sol.islandPerimeter(grid), 10)

	def test_l_shape(self):
		grid = [
			[1, 0],
			[1, 0],
			[1, 1],
		]
		self.assertEqual(self.sol.islandPerimeter(grid), 10)

	def test_zigzag_snake(self):
		grid = [
			[1, 1, 0],
			[0, 1, 1],
			[0, 0, 1],
		]
		self.assertEqual(self.sol.islandPerimeter(grid), 12)

	def test_donut_with_hole(self):
		grid = [
			[1, 1, 1],
			[1, 0, 1],
			[1, 1, 1],
		]
		self.assertEqual(self.sol.islandPerimeter(grid), 16)

	def test_complex_shape_example(self):
		grid = [
			[0, 1, 0, 0],
			[1, 1, 1, 0],
			[0, 1, 0, 0],
			[1, 1, 0, 0],
		]
		self.assertEqual(self.sol.islandPerimeter(grid), 16)

	def test_island_surrounded_by_water(self):
		grid = [
			[0, 0, 0, 0],
			[0, 1, 1, 0],
			[0, 1, 1, 0],
			[0, 0, 0, 0],
		]
		self.assertEqual(self.sol.islandPerimeter(grid), 8)


if __name__ == "__main__":
	unittest.main()
