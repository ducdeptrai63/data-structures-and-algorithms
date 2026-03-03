from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0
        for i in range(len(nums)):
            curr = max(prev1, nums[i] + prev2)
            prev2 = prev1
            prev1 = curr
        return prev1
