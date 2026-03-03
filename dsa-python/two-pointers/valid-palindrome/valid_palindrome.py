class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlnum(c):
            return (ord('a') <= ord(c) <= ord('z') or
                    ord('A') <= ord(c) <= ord('Z') or
                    ord('0') <= ord(c) <= ord('9'))

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not isAlnum(s[l]):
                l += 1
            while l < r and not isAlnum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
