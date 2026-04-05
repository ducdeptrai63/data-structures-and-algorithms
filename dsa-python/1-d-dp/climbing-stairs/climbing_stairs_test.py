import unittest

from climbing_stairs import Solution


class TestClimbingStairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_edge_case_n_1(self):
        """Test the minimum possible constraint n = 1."""
        self.assertEqual(self.solution.climbStairs(1), 1)

    def test_edge_case_n_2(self):
        """Test n = 2."""
        self.assertEqual(self.solution.climbStairs(2), 2)

    def test_typical_case_n_3(self):
        """Test n = 3."""
        self.assertEqual(self.solution.climbStairs(3), 3)

    def test_typical_case_n_5(self):
        """Test n = 5."""
        self.assertEqual(self.solution.climbStairs(5), 8)

    def test_typical_case_n_10(self):
        """Test n = 10."""
        self.assertEqual(self.solution.climbStairs(10), 89)

    def test_edge_case_n_45(self):
        """Test the maximum possible constraint n = 45."""
        self.assertEqual(self.solution.climbStairs(45), 1836311903)


if __name__ == '__main__':
    unittest.main()
