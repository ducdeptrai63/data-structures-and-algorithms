from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tmp = head
        nums = []
        while tmp:
            nums.append(tmp.val)
            tmp = tmp.next

        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] != nums[r]:
                return False
            l += 1
            r -= 1
        return True
