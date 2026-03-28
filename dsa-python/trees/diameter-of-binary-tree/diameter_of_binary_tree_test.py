import unittest

from diameter_of_binary_tree import Solution, TreeNode


class TestDiameterOfBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_node(self):
        root = TreeNode(0)
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 0)

    def test_two_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 1)

    def test_balanced_tree(self):
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3, TreeNode(6), TreeNode(7)),
        )
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 4)

    def test_left_skewed_tree(self):
        root = TreeNode(-1)
        root.left = TreeNode(-2)
        root.left.left = TreeNode(-3)
        root.left.left.left = TreeNode(-4)
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 3)

    def test_right_skewed_tree(self):
        root = TreeNode(10)
        root.right = TreeNode(20)
        root.right.right = TreeNode(30)
        root.right.right.right = TreeNode(40)
        root.right.right.right.right = TreeNode(50)
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 4)

    def test_larger_tree_within_constraints(self):
        # 13 nodes, values within [-100, 100]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)

        root.left.left = TreeNode(4)
        root.left.left.left = TreeNode(6)
        root.left.left.right = TreeNode(7)

        root.left.left.left.left = TreeNode(9)
        root.left.left.left.left.left = TreeNode(11)
        root.left.left.left.left.right = TreeNode(12)
        root.left.left.left.left.right.right = TreeNode(13)

        root.right.right = TreeNode(5)
        root.right.right.right = TreeNode(8)
        root.right.right.right.right = TreeNode(10)

        # Longest path is 13 -> 12 -> 9 -> 6 -> 4 -> 2 -> 1 -> 3 -> 5 -> 8 -> 10
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 10)


if __name__ == "__main__":
    unittest.main()
