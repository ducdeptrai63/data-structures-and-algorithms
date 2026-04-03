class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count1 = 0
        for c in s:
            if c == '1':
                count1 += 1

        return (count1 - 1) * '1' + (len(s) - count1) * '0' + '1'
