import unittest

from palindrome_linked_list import ListNode, Solution


def build_list(values):
    if values is None:
        return None
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


class TestPalindromeLinkedList(unittest.TestCase):
    def run_case(self, values, expected):
        head = build_list(values)
        result = Solution().isPalindrome(head)
        self.assertEqual(result, expected)

    def test_empty_list_is_palindrome(self):
        self.run_case(None, True)

    def test_single_element_is_palindrome(self):
        self.run_case([1], True)

    def test_two_equal_elements_is_palindrome(self):
        self.run_case([7, 7], True)

    def test_two_different_elements_is_not_palindrome(self):
        self.run_case([7, 8], False)

    def test_odd_length_palindrome(self):
        self.run_case([1, 2, 3, 2, 1], True)

    def test_odd_length_non_palindrome(self):
        self.run_case([1, 2, 3, 4, 1], False)

    def test_even_length_palindrome(self):
        self.run_case([1, 2, 2, 1], True)

    def test_even_length_non_palindrome(self):
        self.run_case([1, 2, 3, 4], False)

    def test_repeated_values_palindrome(self):
        self.run_case([5, 5, 5, 5, 5], True)


if __name__ == "__main__":
    unittest.main()
