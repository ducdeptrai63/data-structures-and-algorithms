import unittest

from middle_of_the_linked_list import Solution, ListNode


class TestMiddleOfTheLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def build_list(self, values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def test_single_node(self):
        head = self.build_list([1])
        result = self.solution.middleNode(head)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 1)

    def test_odd_number_of_nodes(self):
        head = self.build_list([1, 2, 3, 4, 5])
        result = self.solution.middleNode(head)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 3)

    def test_even_number_of_nodes(self):
        head = self.build_list([1, 2, 3, 4, 5, 6])
        result = self.solution.middleNode(head)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 4)

    def test_min_and_max_node_values(self):
        head = self.build_list([1, 100, 1])
        result = self.solution.middleNode(head)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 100)

    def test_multiple_sizes(self):
        # Size 2
        head2 = self.build_list([10, 20])
        self.assertEqual(self.solution.middleNode(head2).val, 20)

        # Size 10
        head10 = self.build_list(list(range(1, 11)))
        self.assertEqual(self.solution.middleNode(head10).val, 6)

        # Size 100
        head100 = self.build_list(list(range(1, 101)))
        self.assertEqual(self.solution.middleNode(head100).val, 51)


if __name__ == '__main__':
    unittest.main()
