import unittest

from reverse_linked_list import ListNode, Solution


def build_list(values):
    head = None
    tail = None
    for value in values:
        node = ListNode(value)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head


def to_list(head, max_nodes=1000):
    values = []
    curr = head
    steps = 0
    while curr is not None and steps < max_nodes:
        values.append(curr.val)
        curr = curr.next
        steps += 1
    return values, curr


class TestReverseLinkedList(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty_list(self):
        self.assertIsNone(self.sol.reverseList(None))

    def test_single_node(self):
        head = build_list([1])
        new_head = self.sol.reverseList(head)
        self.assertIsNotNone(new_head)
        self.assertEqual(new_head.val, 1)
        self.assertIsNone(new_head.next)

    def test_two_nodes(self):
        head = build_list([1, 2])
        new_head = self.sol.reverseList(head)
        values, tail = to_list(new_head)
        self.assertEqual(values, [2, 1])
        self.assertIsNone(tail)

    def test_multiple_nodes(self):
        head = build_list([1, 2, 3, 4, 5])
        new_head = self.sol.reverseList(head)
        values, tail = to_list(new_head)
        self.assertEqual(values, [5, 4, 3, 2, 1])
        self.assertIsNone(tail)

    def test_negative_and_zero_values(self):
        head = build_list([0, -1, 2, -3])
        new_head = self.sol.reverseList(head)
        values, tail = to_list(new_head)
        self.assertEqual(values, [-3, 2, -1, 0])
        self.assertIsNone(tail)

    def test_no_cycle_created(self):
        values_in = list(range(10))
        head = build_list(values_in)
        new_head = self.sol.reverseList(head)
        values, tail = to_list(new_head, max_nodes=20)
        self.assertEqual(values, list(reversed(values_in)))
        self.assertIsNone(tail)


if __name__ == "__main__":
    unittest.main()
