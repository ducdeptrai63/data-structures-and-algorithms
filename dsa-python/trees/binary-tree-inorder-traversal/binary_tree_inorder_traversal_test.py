import unittest

from binary_tree_inorder_traversal import Solution, TreeNode


def _n(val, left=None, right=None):
    return TreeNode(val, left, right)


class TestBinaryTreeInorderTraversal(unittest.TestCase):
    def test_inorder_empty_tree(self):
        self.assertEqual(Solution().inorderTraversal(None), [])

    def test_inorder_single_node(self):
        root = _n(1)
        self.assertEqual(Solution().inorderTraversal(root), [1])

    def test_inorder_balanced_tree(self):
        #      4
        #    /   \
        #   2     6
        #  / \   / \
        # 1  3  5  7
        root = _n(4, _n(2, _n(1), _n(3)), _n(6, _n(5), _n(7)))
        self.assertEqual(Solution().inorderTraversal(
            root), [1, 2, 3, 4, 5, 6, 7])

    def test_inorder_left_skewed_tree(self):
        # 3
        # |
        # 2
        # |
        # 1
        root = _n(3, _n(2, _n(1)))
        self.assertEqual(Solution().inorderTraversal(root), [1, 2, 3])

    def test_inorder_right_skewed_tree(self):
        # 1
        #  \
        #   2
        #    \
        #     3
        root = _n(1, None, _n(2, None, _n(3)))
        self.assertEqual(Solution().inorderTraversal(root), [1, 2, 3])

    def test_inorder_with_duplicates_and_negatives(self):
        #      0
        #     / \
        #   -1   1
        #     \   \
        #     -1   1
        root = _n(0, _n(-1, None, _n(-1)), _n(1, None, _n(1)))
        self.assertEqual(Solution().inorderTraversal(root), [-1, -1, 0, 1, 1])


if __name__ == "__main__":
    unittest.main()
