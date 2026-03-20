import unittest

from binary_tree_preorder_traversal import Solution, TreeNode


def _n(val, left=None, right=None):
    return TreeNode(val, left, right)


class TestBinaryTreePreorderTraversal(unittest.TestCase):
    def test_preorder_empty_tree(self):
        self.assertEqual(Solution().preorderTraversal(None), [])

    def test_preorder_single_node(self):
        root = _n(1)
        self.assertEqual(Solution().preorderTraversal(root), [1])

    def test_preorder_left_skewed_tree(self):
        #    1
        #   /
        #  2
        # /
        # 3
        root = _n(1, _n(2, _n(3)))
        self.assertEqual(Solution().preorderTraversal(root), [1, 2, 3])

    def test_preorder_right_skewed_tree(self):
        # 1
        #  \
        #   2
        #    \
        #     3
        root = _n(1, None, _n(2, None, _n(3)))
        self.assertEqual(Solution().preorderTraversal(root), [1, 2, 3])

    def test_preorder_balanced_tree(self):
        #       1
        #     /   \
        #    2     3
        #   / \   / \
        #  4  5  6  7
        root = _n(1, _n(2, _n(4), _n(5)), _n(3, _n(6), _n(7)))
        self.assertEqual(Solution().preorderTraversal(
            root), [1, 2, 4, 5, 3, 6, 7])

    def test_preorder_with_duplicates_and_negatives(self):
        #      0
        #     / \
        #   -1   1
        #     \   \
        #     -1   1
        root = _n(0, _n(-1, None, _n(-1)), _n(1, None, _n(1)))
        self.assertEqual(Solution().preorderTraversal(root), [0, -1, -1, 1, 1])

    def test_preorder_multiple_calls_do_not_share_state(self):
        sol = Solution()

        root1 = _n(1, _n(2), _n(3))
        root2 = _n(9)

        out1 = sol.preorderTraversal(root1)
        out2 = sol.preorderTraversal(root2)

        self.assertEqual(out1, [1, 2, 3])
        self.assertEqual(out2, [9])
        self.assertIsNot(out1, out2)


if __name__ == "__main__":
    unittest.main()
