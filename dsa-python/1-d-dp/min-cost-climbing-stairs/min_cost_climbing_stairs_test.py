import unittest

from min_cost_climbing_stairs import Solution


class TestMinCostClimbingStairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_typical_case_1(self):
        self.assertEqual(self.solution.minCostClimbingStairs([10, 15, 20]), 15)

    def test_typical_case_2(self):
        self.assertEqual(self.solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)

    def test_minimum_length(self):
        self.assertEqual(self.solution.minCostClimbingStairs([0, 0]), 0)
        self.assertEqual(self.solution.minCostClimbingStairs([10, 20]), 10)
        self.assertEqual(self.solution.minCostClimbingStairs([100, 100]), 100)

    def test_maximum_length(self):
        cost_ones = [1] * 100
        self.assertEqual(self.solution.minCostClimbingStairs(cost_ones), 50)
        
        cost_zeroes = [0] * 100
        self.assertEqual(self.solution.minCostClimbingStairs(cost_zeroes), 0)
        
        cost_max = [100] * 100
        self.assertEqual(self.solution.minCostClimbingStairs(cost_max), 5000)

    def test_boundary_values(self):
        self.assertEqual(self.solution.minCostClimbingStairs([0, 100, 0, 100, 0]), 0)
        self.assertEqual(self.solution.minCostClimbingStairs([100, 0, 100, 0, 100]), 0)

    def test_strictly_increasing_costs(self):
        self.assertEqual(self.solution.minCostClimbingStairs([1, 2, 3, 4, 5]), 6)

    def test_strictly_decreasing_costs(self):
        self.assertEqual(self.solution.minCostClimbingStairs([5, 4, 3, 2, 1]), 6)


if __name__ == '__main__':
    unittest.main()
