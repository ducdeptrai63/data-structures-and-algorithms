import unittest

from pascals_triangle import Solution


class TestPascalsTriangle(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def verify_triangle_properties(self, numRows: int, result: list[list[int]]):
        """Helper method to verify all structural requirements of Pascal's Triangle"""
        # Correct triangle structure (number of rows)
        self.assertEqual(len(result), numRows,
                         f"Expected {numRows} rows, got {len(result)}")

        for i in range(numRows):
            # Row length == row_index + 1
            self.assertEqual(len(result[i]), i + 1,
                             f"Row {i} should have length {i + 1}")

            # First and last element of each row == 1
            self.assertEqual(
                result[i][0], 1, f"First element of row {i} should be 1")
            self.assertEqual(result[i][-1], 1,
                             f"Last element of row {i} should be 1")

            # Inner values follow Pascal rule: C[i][j] = C[i-1][j-1] + C[i-1][j]
            for j in range(1, i):
                expected_val = result[i - 1][j - 1] + result[i - 1][j]
                self.assertEqual(
                    result[i][j],
                    expected_val,
                    f"Pascal rule failed at row {i}, col {j}. Expected {expected_val}, got {result[i][j]}"
                )

    def test_minimum_case_1(self):
        numRows = 1
        result = self.solution.generate(numRows)
        self.assertEqual(result, [[1]])
        self.verify_triangle_properties(numRows, result)

    def test_small_typical_case_2(self):
        numRows = 2
        result = self.solution.generate(numRows)
        self.assertEqual(result, [[1], [1, 1]])
        self.verify_triangle_properties(numRows, result)

    def test_small_typical_case_3(self):
        numRows = 3
        result = self.solution.generate(numRows)
        self.assertEqual(result, [[1], [1, 1], [1, 2, 1]])
        self.verify_triangle_properties(numRows, result)

    def test_small_typical_case_5(self):
        numRows = 5
        result = self.solution.generate(numRows)
        self.assertEqual(
            result,
            [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        )
        self.verify_triangle_properties(numRows, result)

    def test_medium_case_10(self):
        numRows = 10
        result = self.solution.generate(numRows)
        self.verify_triangle_properties(numRows, result)

        # Additional check for a known value C(9, 4) = 126
        self.assertEqual(result[9][4], 126)

    def test_upper_bound_30(self):
        numRows = 30
        result = self.solution.generate(numRows)
        self.verify_triangle_properties(numRows, result)

        # Additional check for a known value C(29, 14) = 77558760
        self.assertEqual(result[29][14], 77558760)


if __name__ == '__main__':
    unittest.main()
