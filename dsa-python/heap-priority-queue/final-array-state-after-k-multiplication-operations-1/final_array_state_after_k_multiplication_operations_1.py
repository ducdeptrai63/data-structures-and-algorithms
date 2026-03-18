import heapq
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        res = nums[:]

        heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)

        for _ in range(k):
            num, i = heapq.heappop(heap)
            res[i] *= multiplier
            heapq.heappush(heap, (res[i], i))

        return res
