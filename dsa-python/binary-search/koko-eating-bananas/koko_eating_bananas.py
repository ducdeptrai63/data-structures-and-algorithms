from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l <= r:
            m = int((l + r) / 2)

            hrs = 0
            for pile in piles:
                hrs += (pile + m - 1) // m

            if hrs > h:
                l = m + 1
            else:
                r = m - 1

        return l
