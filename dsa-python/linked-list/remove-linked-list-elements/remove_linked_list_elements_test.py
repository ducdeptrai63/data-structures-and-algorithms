import unittest

from remove_linked_list_elements import ListNode, Solution


def build_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def to_pylist(head, max_steps=10_000):
    out = []
    seen = set()
    steps = 0
    curr = head
    while curr is not None:
        node_id = id(curr)
        if node_id in seen:
            raise AssertionError("Cycle detected in linked list")
        seen.add(node_id)

        out.append(curr.val)
        curr = curr.next
        steps += 1
        if steps > max_steps:
            raise AssertionError(
                "Traversal exceeded max_steps (possible cycle)")
    return out


def nodes_in_order(head, max_steps=10_000):
    out = []
    seen = set()
    steps = 0
    curr = head
    while curr is not None:
        node_id = id(curr)
        if node_id in seen:
            raise AssertionError("Cycle detected in linked list")
        seen.add(node_id)

        out.append(curr)
        curr = curr.next
        steps += 1
        if steps > max_steps:
            raise AssertionError(
                "Traversal exceeded max_steps (possible cycle)")
    return out


class TestRemoveLinkedListElements(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list_returns_none(self):
        out = self.solution.removeElements(None, 1)
        self.assertIsNone(out)
        self.assertEqual(to_pylist(out), [])

    def test_no_matches_keeps_same_head_and_values(self):
        head = build_list([1, 2, 3, 4])
        out = self.solution.removeElements(head, 99)

        self.assertIs(out, head)
        self.assertEqual(to_pylist(out), [1, 2, 3, 4])

    def test_all_match_returns_none(self):
        head = build_list([7, 7, 7, 7])
        out = self.solution.removeElements(head, 7)

        self.assertIsNone(out)
        self.assertEqual(to_pylist(out), [])

    def test_remove_from_head(self):
        head = build_list([6, 1, 2, 3])
        out = self.solution.removeElements(head, 6)
        self.assertEqual(to_pylist(out), [1, 2, 3])

    def test_remove_from_tail(self):
        head = build_list([1, 2, 3, 6])
        out = self.solution.removeElements(head, 6)
        self.assertEqual(to_pylist(out), [1, 2, 3])

    def test_remove_multiple_and_consecutive_occurrences(self):
        head = build_list([1, 6, 6, 2, 6, 3, 6])
        out = self.solution.removeElements(head, 6)
        self.assertEqual(to_pylist(out), [1, 2, 3])

    def test_leetcode_example(self):
        head = build_list([1, 2, 6, 3, 4, 5, 6])
        out = self.solution.removeElements(head, 6)
        self.assertEqual(to_pylist(out), [1, 2, 3, 4, 5])

    def test_remove_zeros(self):
        head = build_list([0, 1, 0, 2, 0])
        out = self.solution.removeElements(head, 0)
        self.assertEqual(to_pylist(out), [1, 2])

    def test_remove_negative_values(self):
        head = build_list([-1, -2, -1, 3])
        out = self.solution.removeElements(head, -1)
        self.assertEqual(to_pylist(out), [-2, 3])

    def test_single_element_removed_returns_none(self):
        head = build_list([6])
        out = self.solution.removeElements(head, 6)

        self.assertIsNone(out)
        self.assertEqual(to_pylist(out), [])

    def test_single_element_not_removed_kept(self):
        head = build_list([6])
        out = self.solution.removeElements(head, 1)

        self.assertIs(out, head)
        self.assertEqual(to_pylist(out), [6])

    def test_preserves_node_identity_for_retained_nodes(self):
        head = build_list([1, 2, 6, 3, 6, 4])

        original_nodes = nodes_in_order(head)
        original_kept = [n for n in original_nodes if n.val != 6]
        original_kept_ids = [id(n) for n in original_kept]
        original_kept_vals = [n.val for n in original_kept]

        out = self.solution.removeElements(head, 6)
        out_nodes = nodes_in_order(out)

        self.assertEqual([n.val for n in out_nodes], original_kept_vals)
        self.assertEqual([id(n) for n in out_nodes], original_kept_ids)

    def test_does_not_introduce_cycles(self):
        head = build_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
        out = self.solution.removeElements(head, 5)

        # to_pylist will fail if a cycle is present
        self.assertEqual(to_pylist(out, max_steps=100),
                         [1, 2, 3, 4, 6, 7, 8, 9])


if __name__ == "__main__":
    unittest.main()
