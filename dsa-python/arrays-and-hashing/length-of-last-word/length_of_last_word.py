class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while s[i] == " ":
            i -= 1

        res = 0
        while s[i] != " " and i >= 0:
            res += 1
            i -= 1

        return res
