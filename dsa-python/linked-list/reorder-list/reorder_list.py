from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        slow.next = None

        fst = head
        snd = prev
        while snd:
            fst_next = fst.next
            snd_next = snd.next

            fst.next = snd
            snd.next = fst_next

            fst = fst_next
            snd = snd_next
