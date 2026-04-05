from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost1 = 0
        cost2 = 0

        for i in range(2, len(cost) + 1):
            min_cost = min(cost1 + cost[i - 1], cost2 + cost[i - 2])
            cost2 = cost1
            cost1 = min_cost

        return cost1