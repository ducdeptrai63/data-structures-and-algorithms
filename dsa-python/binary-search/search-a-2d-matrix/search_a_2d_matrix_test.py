import unittest

from search_a_2d_matrix import Solution


class TestSearchMatrix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_valid_case_target_exists(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        self.assertTrue(self.solution.searchMatrix(matrix, 3))

    def test_target_does_not_exist(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        self.assertFalse(self.solution.searchMatrix(matrix, 13))

    def test_edge_case_1x1(self):
        matrix = [[1]]
        self.assertTrue(self.solution.searchMatrix(matrix, 1))
        self.assertFalse(self.solution.searchMatrix(matrix, 2))

    def test_edge_case_1xn(self):
        matrix = [[1, 3, 5, 7, 9]]
        self.assertTrue(self.solution.searchMatrix(matrix, 5))
        self.assertFalse(self.solution.searchMatrix(matrix, 6))

    def test_edge_case_mx1(self):
        matrix = [[1], [3], [5], [7], [9]]
        self.assertTrue(self.solution.searchMatrix(matrix, 5))
        self.assertFalse(self.solution.searchMatrix(matrix, 6))

    def test_boundary_values(self):
        matrix = [[-10000, -5000, 0], [10, 50, 10000]]
        self.assertTrue(self.solution.searchMatrix(matrix, -10000))
        self.assertTrue(self.solution.searchMatrix(matrix, 10000))
        self.assertFalse(self.solution.searchMatrix(matrix, -10001))
        self.assertFalse(self.solution.searchMatrix(matrix, 10001))

    def test_larger_matrix_within_constraints(self):
        m, n = 100, 100
        # Creating a 100x100 sorted matrix with values in range constraint
        matrix = [[i * n + j - 5000 for j in range(n)] for i in range(m)]

        # Test targets that exist
        self.assertTrue(self.solution.searchMatrix(matrix, matrix[50][50]))
        self.assertTrue(self.solution.searchMatrix(matrix, matrix[0][0]))
        self.assertTrue(self.solution.searchMatrix(
            matrix, matrix[m - 1][n - 1]))

        # Test targets that do not exist
        self.assertFalse(self.solution.searchMatrix(matrix, -10000))
        self.assertFalse(self.solution.searchMatrix(matrix, 10000))


if __name__ == '__main__':
    unittest.main()
