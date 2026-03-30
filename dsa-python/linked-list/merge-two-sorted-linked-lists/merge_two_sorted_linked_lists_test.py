import unittest

from merge_two_sorted_linked_lists import Solution, ListNode


def list_to_linked_list(values):
    if not values:
        return None
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def linked_list_to_list(head):
    out = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out


class TestMergeTwoSortedLinkedLists(unittest.TestCase):
    def setUp(self):
        self.sut = Solution()

    def test_both_lists_empty(self):
        result = self.sut.mergeTwoLists(None, None)
        self.assertEqual(linked_list_to_list(result), [])

    def test_one_list_empty_left(self):
        list2 = list_to_linked_list([1, 2, 3])
        result = self.sut.mergeTwoLists(None, list2)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3])

    def test_one_list_empty_right(self):
        list1 = list_to_linked_list([1, 2, 3])
        result = self.sut.mergeTwoLists(list1, None)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3])

    def test_single_element_lists_in_order(self):
        list1 = list_to_linked_list([1])
        list2 = list_to_linked_list([2])
        result = self.sut.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [1, 2])

    def test_single_element_lists_reverse_order(self):
        list1 = list_to_linked_list([2])
        list2 = list_to_linked_list([1])
        result = self.sut.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [1, 2])

    def test_single_element_lists_equal(self):
        list1 = list_to_linked_list([0])
        list2 = list_to_linked_list([0])
        result = self.sut.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [0, 0])

    def test_different_lengths(self):
        a = [1, 2, 4]
        b = [1, 3, 4, 5, 6]
        list1 = list_to_linked_list(a)
        list2 = list_to_linked_list(b)
        result = self.sut.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), sorted(a + b))

    def test_already_interleaved_values(self):
        a = [1, 3, 5]
        b = [2, 4, 6]
        list1 = list_to_linked_list(a)
        list2 = list_to_linked_list(b)
        result = self.sut.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3, 4, 5, 6])

    def test_all_elements_equal(self):
        a = [7, 7, 7]
        b = [7, 7]
        list1 = list_to_linked_list(a)
        list2 = list_to_linked_list(b)
        result = self.sut.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [7, 7, 7, 7, 7])

    def test_negative_values(self):
        a = [-10, -5, -1]
        b = [-9, -6, -2]
        list1 = list_to_linked_list(a)
        list2 = list_to_linked_list(b)
        result = self.sut.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), sorted(a + b))

    def test_boundary_values_negative_100_and_100(self):
        a = [-100, 0, 100]
        b = [-100, 100]
        list1 = list_to_linked_list(a)
        list2 = list_to_linked_list(b)
        result = self.sut.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), sorted(a + b))
        self.assertIn(-100, linked_list_to_list(result))
        self.assertIn(100, linked_list_to_list(result))

    def test_maximum_size_lists_length_100_each(self):
        # length 100, values within [-100, 100], sorted
        a = list(range(-100, 100, 2))   # -100, -98, ..., 98 (100 items)
        b = list(range(-99, 101, 2))    # -99, -97, ..., 99 (100 items)
        self.assertEqual(len(a), 100)
        self.assertEqual(len(b), 100)

        list1 = list_to_linked_list(a)
        list2 = list_to_linked_list(b)
        result = self.sut.mergeTwoLists(list1, list2)

        out = linked_list_to_list(result)
        expected = sorted(a + b)

        self.assertEqual(len(out), 200)
        self.assertEqual(out, expected)


if __name__ == "__main__":
    unittest.main()
