from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for log in logs:
            if log == '../':
                if res:
                    res -= 1
            elif log != './':
                res += 1
        return res
