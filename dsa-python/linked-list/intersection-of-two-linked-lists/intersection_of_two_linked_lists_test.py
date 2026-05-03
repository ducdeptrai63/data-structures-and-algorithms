import unittest

from intersection_of_two_linked_lists import Solution, ListNode


class TestIntersectionOfTwoLinkedLists(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def build_lists(self, listA_vals, listB_vals, skipA, skipB):
        """
        Helper method to construct listA and listB which may intersect.
        """
        headA, headB = None, None
        currA, currB = None, None

        # Build A up to skipA
        for i in range(skipA):
            node = ListNode(listA_vals[i])
            if not headA:
                headA = node
                currA = headA
            else:
                currA.next = node
                currA = currA.next

        # Build B up to skipB
        for i in range(skipB):
            node = ListNode(listB_vals[i])
            if not headB:
                headB = node
                currB = headB
            else:
                currB.next = node
                currB = currB.next

        # Build intersection part
        intersection_head = None
        curr_inter = None
        for i in range(skipA, len(listA_vals)):
            node = ListNode(listA_vals[i])
            if not intersection_head:
                intersection_head = node
                curr_inter = intersection_head
            else:
                curr_inter.next = node
                curr_inter = curr_inter.next

        # Connect A to the intersection
        if currA:
            currA.next = intersection_head
        else:
            headA = intersection_head

        # Connect B to the intersection
        if currB:
            currB.next = intersection_head
        else:
            headB = intersection_head

        return headA, headB, intersection_head

    def test_no_intersection(self):
        # listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
        headA, headB, _ = self.build_lists([2, 6, 4], [1, 5], 3, 2)
        result = self.solution.getIntersectionNode(headA, headB)
        self.assertIsNone(result)

    def test_intersect_at_head(self):
        # listA = [1,2,3], listB = [1,2,3], skipA = 0, skipB = 0
        headA, headB, expected = self.build_lists([1, 2, 3], [1, 2, 3], 0, 0)
        result = self.solution.getIntersectionNode(headA, headB)
        self.assertIs(result, expected)

    def test_intersect_at_middle(self):
        # listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
        headA, headB, expected = self.build_lists(
            [4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 2, 3)
        result = self.solution.getIntersectionNode(headA, headB)
        self.assertIs(result, expected)

    def test_intersect_at_tail(self):
        # listA = [1,2,3], listB = [4,5,3], skipA = 2, skipB = 2
        headA, headB, expected = self.build_lists([1, 2, 3], [4, 5, 3], 2, 2)
        result = self.solution.getIntersectionNode(headA, headB)
        self.assertIs(result, expected)

    def test_minimum_size(self):
        # Case minimum size: len=1, no intersect
        headA, headB, _ = self.build_lists([1], [2], 1, 1)
        result = self.solution.getIntersectionNode(headA, headB)
        self.assertIsNone(result)

        # Case minimum size: len=1, intersect
        headA, headB, expected = self.build_lists([1], [1], 0, 0)
        result = self.solution.getIntersectionNode(headA, headB)
        self.assertIs(result, expected)

    def test_large_input(self):
        # Performance boundary: m = 30000, n = 30000, intersect at end
        listA_vals = [1] * 30000
        listB_vals = [2] * 30000
        listA_vals[-1] = 99999
        listB_vals[-1] = 99999

        headA, headB, expected = self.build_lists(
            listA_vals, listB_vals, 29999, 29999)
        result = self.solution.getIntersectionNode(headA, headB)
        self.assertIs(result, expected)
        if expected:
            self.assertEqual(result.val, 99999)


if __name__ == '__main__':
    unittest.main()
