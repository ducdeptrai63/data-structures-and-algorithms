from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = cnt = 0
        for num in nums:
            cnt = 0 if num == 0 else cnt + 1
            res = max(res, cnt)
        return res
