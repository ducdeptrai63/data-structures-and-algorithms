from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0

        while i < len(nums):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]

                if three_sum > 0:
                    k -= 1
                elif three_sum < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

            i += 1

        return res
