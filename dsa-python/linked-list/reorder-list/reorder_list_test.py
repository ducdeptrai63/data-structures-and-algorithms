import unittest

from reorder_list import Solution, ListNode


def create_list(values):
    """Helper to convert list of values to linked list"""
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def list_to_array(head):
    """Helper to convert linked list to list of values"""
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res


class TestReorderList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_min_length_list(self):
        head = create_list([1])
        self.solution.reorderList(head)
        self.assertEqual(list_to_array(head), [1])

    def test_even_length_list(self):
        head = create_list([1, 2, 3, 4])
        self.solution.reorderList(head)
        self.assertEqual(list_to_array(head), [1, 4, 2, 3])

    def test_odd_length_list(self):
        head = create_list([1, 2, 3, 4, 5])
        self.solution.reorderList(head)
        self.assertEqual(list_to_array(head), [1, 5, 2, 4, 3])

    def test_larger_list_cases(self):
        # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        head = create_list(list(range(1, 11)))
        self.solution.reorderList(head)
        self.assertEqual(list_to_array(head), [1, 10, 2, 9, 3, 8, 4, 7, 5, 6])

    def test_edge_value_cases(self):
        # Using minimum and maximum values specified (1 and 1000)
        head = create_list([1, 500, 1000])
        self.solution.reorderList(head)
        self.assertEqual(list_to_array(head), [1, 1000, 500])

        head2 = create_list([1000, 1, 1000, 1])
        self.solution.reorderList(head2)
        self.assertEqual(list_to_array(head2), [1000, 1, 1, 1000])


if __name__ == '__main__':
    unittest.main()
