from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def bs(arr, target):
            l, r = 0, len(arr)

            while l < r:
                m = int((l + r) / 2)

                if arr[m] < target:
                    l = m + 1
                else:
                    r = m
            return l

        sub = []

        for num in nums:
            pos = bs(sub, num)

            if pos == len(sub):
                sub.append(num)
            else:
                sub[pos] = num

        return len(sub)
