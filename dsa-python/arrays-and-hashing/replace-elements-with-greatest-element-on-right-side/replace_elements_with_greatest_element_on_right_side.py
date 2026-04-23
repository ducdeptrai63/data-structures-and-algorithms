from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        rightMax = -1

        for i in range(n - 1, -1, -1):
            tmp = arr[i]
            arr[i] = rightMax
            rightMax = max(rightMax, tmp)

        return arr
