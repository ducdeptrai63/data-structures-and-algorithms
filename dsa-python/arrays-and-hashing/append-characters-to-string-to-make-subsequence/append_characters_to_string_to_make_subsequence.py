class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n = len(t)
        i = 0
        for c in s:
            if i < n and c == t[i]:
                i += 1
        return n - i
