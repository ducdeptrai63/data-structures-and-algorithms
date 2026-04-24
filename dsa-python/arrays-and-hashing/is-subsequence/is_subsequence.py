class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        matched = 0
        for c in t:
            if matched < len(s) and s[matched] == c:
                matched += 1
        return matched == len(s)
