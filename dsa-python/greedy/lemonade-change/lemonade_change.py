from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cnt5 = cnt10 = 0

        for b in bills:
            if b == 5:
                cnt5 += 1
            elif b == 10:
                if cnt5 > 0:
                    cnt10 += 1
                    cnt5 -= 1
                else:
                    return False
            else:
                if cnt10 > 0 and cnt5 > 0:
                    cnt10 -= 1
                    cnt5 -= 1
                elif cnt5 > 2:
                    cnt5 -= 3
                else:
                    return False
        return True
