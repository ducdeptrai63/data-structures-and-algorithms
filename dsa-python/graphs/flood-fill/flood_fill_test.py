import unittest

from flood_fill import Solution


class TestFloodFill(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_standard_example_changes_connected_region_only(self):
        image = [
                [1, 1, 1],
                [1, 1, 0],
                [1, 0, 1],
        ]
        expected = [
            [2, 2, 2],
            [2, 2, 0],
            [2, 0, 1],
        ]

        result = self.solution.floodFill(image, 1, 1, 2)

        self.assertIs(result, image)
        self.assertEqual(result, expected)

    def test_no_op_when_target_already_new_color_returns_same_image_unchanged(self):
        image = [
                [5, 5, 5],
                [5, 5, 0],
                [5, 0, 5],
        ]
        before = [row[:] for row in image]

        result = self.solution.floodFill(image, 0, 0, 5)

        self.assertIs(result, image)
        self.assertEqual(result, before)
        self.assertEqual(image, before)

    def test_does_not_fill_diagonals_only_center_changes(self):
        image = [
                [1, 0, 1],
                [0, 1, 0],
                [1, 0, 1],
        ]
        expected = [
            [1, 0, 1],
            [0, 2, 0],
            [1, 0, 1],
        ]

        result = self.solution.floodFill(image, 1, 1, 2)

        self.assertIs(result, image)
        self.assertEqual(result, expected)

    def test_from_border_fills_connected_border_region_stops_at_barriers(self):
        image = [
                [3, 3, 3, 3],
                [3, 1, 1, 3],
                [3, 1, 2, 3],
                [3, 3, 3, 3],
        ]
        expected = [
            [9, 9, 9, 9],
            [9, 1, 1, 9],
            [9, 1, 2, 9],
            [9, 9, 9, 9],
        ]

        result = self.solution.floodFill(image, 0, 0, 9)

        self.assertIs(result, image)
        self.assertEqual(result, expected)

    def test_single_cell_image_recolors_that_cell(self):
        image = [[7]]
        expected = [[8]]

        result = self.solution.floodFill(image, 0, 0, 8)

        self.assertIs(result, image)
        self.assertEqual(result, expected)

    def test_only_recolors_component_containing_start_not_other_same_values_elsewhere(self):
        image = [
                [1, 1, 0, 1],
                [1, 0, 0, 1],
                [1, 1, 0, 1],
        ]
        expected = [
            [2, 2, 0, 1],
            [2, 0, 0, 1],
            [2, 2, 0, 1],
        ]

        result = self.solution.floodFill(image, 0, 0, 2)

        self.assertIs(result, image)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
