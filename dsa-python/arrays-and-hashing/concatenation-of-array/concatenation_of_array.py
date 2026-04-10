from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums.copy()
        for num in nums:
            ans.append(num)
        return ans
