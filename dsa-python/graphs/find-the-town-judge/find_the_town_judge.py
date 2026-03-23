from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        score = [0] * (n + 1)

        for truster, trusted in trust:
            score[truster] -= 1
            score[trusted] += 1

        for person in range(1, n + 1):
            if score[person] == n - 1:
                return person

        return -1
