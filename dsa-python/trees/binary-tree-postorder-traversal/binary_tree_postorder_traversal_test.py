import unittest

from binary_tree_postorder_traversal import Solution, TreeNode


def _n(val, left=None, right=None):
    return TreeNode(val, left, right)


def _ref_postorder(root):
    if root is None:
        return []
    return _ref_postorder(root.left) + _ref_postorder(root.right) + [root.val]


class TestBinaryTreePostorderTraversal(unittest.TestCase):
    def test_postorder_empty_tree(self):
        self.assertEqual(Solution().postorderTraversal(None), [])

    def test_postorder_single_node(self):
        root = _n(42)
        self.assertEqual(Solution().postorderTraversal(root), [42])

    def test_postorder_left_skewed_tree(self):
        #    1
        #   /
        #  2
        # /
        # 3
        root = _n(1, _n(2, _n(3)))
        self.assertEqual(Solution().postorderTraversal(root), [3, 2, 1])

    def test_postorder_right_skewed_tree(self):
        # 1
        #  \
        #   2
        #    \
        #     3
        root = _n(1, None, _n(2, None, _n(3)))
        self.assertEqual(Solution().postorderTraversal(root), [3, 2, 1])

    def test_postorder_balanced_tree(self):
        #       1
        #     /   \
        #    2     3
        #   / \   / \
        #  4  5  6  7
        root = _n(1, _n(2, _n(4), _n(5)), _n(3, _n(6), _n(7)))
        self.assertEqual(Solution().postorderTraversal(
            root), [4, 5, 2, 6, 7, 3, 1])

    def test_postorder_with_duplicates(self):
        #     1
        #    / \
        #   1   1
        #      /
        #     1
        root = _n(1, _n(1), _n(1, _n(1), None))
        self.assertEqual(Solution().postorderTraversal(root), [1, 1, 1, 1])

    def test_postorder_with_negative_and_zero_values(self):
        #      0
        #     / \
        #   -1   2
        #     \
        #     -3
        root = _n(0, _n(-1, None, _n(-3)), _n(2))
        self.assertEqual(Solution().postorderTraversal(root), [-3, -1, 2, 0])

    def test_postorder_multiple_calls_do_not_share_state(self):
        sol = Solution()

        root1 = _n(1, _n(2), _n(3))
        root2 = _n(9)

        out1 = sol.postorderTraversal(root1)
        out2 = sol.postorderTraversal(root2)

        self.assertEqual(out1, [2, 3, 1])
        self.assertEqual(out2, [9])
        self.assertIsNot(out1, out2)

    def test_postorder_larger_complete_tree_matches_reference(self):
        # Build a complete binary tree with values 1..31 (depth 5).
        nodes = [None] + [_n(i) for i in range(1, 32)]
        for i in range(1, 16):
            nodes[i].left = nodes[2 * i]
            nodes[i].right = nodes[2 * i + 1]

        root = nodes[1]
        expected = _ref_postorder(root)
        result = Solution().postorderTraversal(root)

        self.assertEqual(result, expected)
        self.assertEqual(len(result), 31)
        self.assertEqual(result[-1], 1)


if __name__ == "__main__":
    unittest.main()
