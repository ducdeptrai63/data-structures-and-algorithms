from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[-1]

        def findMax(idx1, idx2):
            rob1, rob2 = 0, 0

            for idx in range(idx1, idx2):
                newRob = max(rob1, nums[idx] + rob2)
                rob2 = rob1
                rob1 = newRob

            return rob1

        return max(findMax(0, len(nums) - 1), findMax(1, len(nums)))
