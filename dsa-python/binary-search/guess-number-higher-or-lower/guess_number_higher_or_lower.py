class Solution:
    def __init__(self, picked: int):
        self.picked = picked

    # @param num, your guess
    # @return -1 if num is higher than the picked number
    #          1 if num is lower than the picked number
    #          otherwise return 0
    def guess(self, num: int) -> int:
        if num > self.picked:
            return -1
        elif num < self.picked:
            return 1
        return 0

    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            m = (l + r) // 2
            if self.guess(m) > 0:
                l = m + 1
            else:
                r = m
        return l
