from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1 for _ in range(i + 1)] for i in range(numRows)]

        for i in range(2, numRows):
            for j in range(1, len(res[i]) - 1):
                res[i][j] = res[i - 1][j] + res[i - 1][j - 1]

        return res
