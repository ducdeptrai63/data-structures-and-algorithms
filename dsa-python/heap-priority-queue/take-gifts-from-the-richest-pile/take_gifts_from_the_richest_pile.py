import heapq
from math import isqrt
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)

        for _ in range(k):
            tmp = -heapq.heappop(gifts)
            heapq.heappush(gifts, -isqrt(tmp))
        return -sum(gifts)
