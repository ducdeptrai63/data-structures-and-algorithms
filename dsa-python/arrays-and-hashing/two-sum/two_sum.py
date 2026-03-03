from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # val -> index

        for idx, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], idx]
            seen[num] = idx
