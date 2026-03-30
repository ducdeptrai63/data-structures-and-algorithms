import unittest

from linked_list_cycle_detection import ListNode, Solution


def build_linked_list(values, pos):
    if not values:
        return None

    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        if pos < 0 or pos >= len(nodes):
            raise ValueError(
                "pos must be -1 or a valid index in the linked list")
        nodes[-1].next = nodes[pos]

    return nodes[0]


class TestLinkedListCycleDetection(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        head = build_linked_list([], -1)
        self.assertFalse(self.solution.hasCycle(head))

    def test_single_node_without_cycle(self):
        head = build_linked_list([0], -1)
        self.assertFalse(self.solution.hasCycle(head))

    def test_single_node_with_self_cycle(self):
        head = build_linked_list([0], 0)
        self.assertTrue(self.solution.hasCycle(head))

    def test_multiple_nodes_without_cycle(self):
        head = build_linked_list([1, 2, 3, 4, 5], -1)
        self.assertFalse(self.solution.hasCycle(head))

    def test_cycle_at_head_index_0(self):
        head = build_linked_list([10, 20, 30, 40], 0)
        self.assertTrue(self.solution.hasCycle(head))

    def test_cycle_in_middle(self):
        head = build_linked_list([1, 2, 3, 4, 5, 6], 2)
        self.assertTrue(self.solution.hasCycle(head))

    def test_cycle_at_last_node_pointing_to_valid_index(self):
        head = build_linked_list([7, 8, 9, 10], 1)
        self.assertTrue(self.solution.hasCycle(head))

    def test_maximum_length_1000_nodes(self):
        values = list(range(1000))  # within [-1000, 1000]
        head_no_cycle = build_linked_list(values, -1)
        self.assertFalse(self.solution.hasCycle(head_no_cycle))

        head_with_cycle = build_linked_list(values, 500)
        self.assertTrue(self.solution.hasCycle(head_with_cycle))

    def test_values_at_boundaries_no_cycle(self):
        head = build_linked_list([-1000, 0, 1000], -1)
        self.assertFalse(self.solution.hasCycle(head))

    def test_values_at_boundaries_with_cycle(self):
        head = build_linked_list([-1000, 1000], 0)
        self.assertTrue(self.solution.hasCycle(head))


if __name__ == "__main__":
    unittest.main()
