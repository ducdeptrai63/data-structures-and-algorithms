import unittest

from typing import Optional
from remove_duplicates_from_sorted_list import ListNode, Solution


def list_to_linked_list(lst: list) -> Optional[ListNode]:
    """Helper function to convert a Python list to a linked list."""
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(node: Optional[ListNode]) -> list:
    """Helper function to convert a linked list back to a Python list."""
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res


class TestRemoveDuplicatesFromSortedList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        head = list_to_linked_list([])
        result = self.solution.deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(result), [])

    def test_single_node(self):
        head = list_to_linked_list([1])
        result = self.solution.deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(result), [1])

    def test_all_duplicates(self):
        head = list_to_linked_list([2, 2, 2, 2])
        result = self.solution.deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(result), [2])

    def test_no_duplicates(self):
        head = list_to_linked_list([-10, 0, 10, 20])
        result = self.solution.deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(result), [-10, 0, 10, 20])

    def test_mixed_duplicates(self):
        head = list_to_linked_list([1, 1, 2, 3, 3])
        result = self.solution.deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3])

        head2 = list_to_linked_list([1, 1, 2])
        result2 = self.solution.deleteDuplicates(head2)
        self.assertEqual(linked_list_to_list(result2), [1, 2])

    def test_negative_values(self):
        head = list_to_linked_list([-100, -100, -50, 0, 0, 50, 100, 100])
        result = self.solution.deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(result), [-100, -50, 0, 50, 100])

    def test_large_list(self):
        # Create a list of 300 elements with duplicates e.g., 0, 0, 1, 1, ...
        input_list = sorted([i // 2 for i in range(300)])
        expected_output = list(range(150))
        head = list_to_linked_list(input_list)
        result = self.solution.deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(result), expected_output)


if __name__ == '__main__':
    unittest.main()
