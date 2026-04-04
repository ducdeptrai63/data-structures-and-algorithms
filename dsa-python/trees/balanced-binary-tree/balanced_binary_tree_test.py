import unittest

from balanced_binary_tree import Solution, TreeNode


def build_level_order(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        current = queue.pop(0)
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    return root


class TestBalancedBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        root = build_level_order([])
        self.assertTrue(self.solution.isBalanced(root))

    def test_single_node(self):
        root = build_level_order([1])
        self.assertTrue(self.solution.isBalanced(root))

    def test_balanced_complete(self):
        root = build_level_order([1, 2, 3, 4, 5, 6, 7])
        self.assertTrue(self.solution.isBalanced(root))

    def test_balanced_not_complete(self):
        root = build_level_order([1, 2, 3, 4, 5, None, 7])
        self.assertTrue(self.solution.isBalanced(root))

    def test_unbalanced_tree(self):
        root = build_level_order([1, 2, 2, 3, 3, None, None, 4, 4])
        self.assertFalse(self.solution.isBalanced(root))

    def test_left_skewed(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        self.assertFalse(self.solution.isBalanced(root))

    def test_right_skewed(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.assertFalse(self.solution.isBalanced(root))

    def test_negative_values(self):
        root = build_level_order([-1, -2, -3, -4, -5, None, -7])
        self.assertTrue(self.solution.isBalanced(root))

    def test_large_tree_near_upper_constraint(self):
        values = list(range(1000))
        root = build_level_order(values)
        self.assertTrue(self.solution.isBalanced(root))


if __name__ == '__main__':
    unittest.main()
