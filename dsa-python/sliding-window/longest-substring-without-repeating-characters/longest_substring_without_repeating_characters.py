class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = res = 0

        for r in range(len(s)):
            if s[r] in seen:
                l = max(l, seen[s[r]] + 1)

            seen[s[r]] = r
            res = max(res, r - l + 1)
        return res
