from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin = 1, 1
        res = nums[0]

        for num in nums:
            tmp = currMax * num
            currMax = max(num, num * currMax, num * currMin)
            currMin = min(num, tmp, num * currMin)
            res = max(res, currMax)
        return res
