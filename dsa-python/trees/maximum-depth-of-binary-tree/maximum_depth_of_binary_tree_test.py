import unittest

from maximum_depth_of_binary_tree import Solution, TreeNode


def build_tree_from_list(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    index = 1

    while queue and index < len(values):
        node = queue.pop(0)

        if index < len(values):
            left_val = values[index]
            index += 1
            if left_val is not None:
                node.left = TreeNode(left_val)
                queue.append(node.left)

        if index < len(values):
            right_val = values[index]
            index += 1
            if right_val is not None:
                node.right = TreeNode(right_val)
                queue.append(node.right)

    return root


class TestMaximumDepthOfBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        self.assertEqual(self.solution.maxDepth(None), 0)

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.maxDepth(root), 1)

    def test_balanced_tree(self):
        root = build_tree_from_list([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(self.solution.maxDepth(root), 3)

    def test_left_skewed_tree(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
        self.assertEqual(self.solution.maxDepth(root), 4)

    def test_right_skewed_tree(self):
        root = TreeNode(1, None, TreeNode(
            2, None, TreeNode(3, None, TreeNode(4))))
        self.assertEqual(self.solution.maxDepth(root), 4)

    def test_unbalanced_right_deeper(self):
        root = TreeNode(1, TreeNode(2), TreeNode(
            3, None, TreeNode(4, None, TreeNode(5))))
        self.assertEqual(self.solution.maxDepth(root), 4)

    def test_mixed_structure(self):
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(4)),
            TreeNode(3, None, TreeNode(5, TreeNode(6))),
        )
        self.assertEqual(self.solution.maxDepth(root), 4)


if __name__ == "__main__":
    unittest.main()
