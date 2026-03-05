class Solution:
    def isValid(self, s: str) -> bool:
        mp = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for c in s:
            if c in mp:
                stack.append(c)
            else:
                if not stack or mp[stack.pop()] != c:
                    return False

        return not stack
