import unittest

from invert_binary_tree import Solution, TreeNode


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


def to_list_level_order(root):
    if root is None:
        return []

    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            result.append(None)
            continue

        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)

    while result and result[-1] is None:
        result.pop()

    return result


class TestInvertBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        self.assertIsNone(self.solution.invertTree(None))

    def test_single_node(self):
        root = TreeNode(1)
        inverted = self.solution.invertTree(root)
        self.assertIs(inverted, root)
        self.assertEqual(inverted.val, 1)
        self.assertIsNone(inverted.left)
        self.assertIsNone(inverted.right)

    def test_three_nodes(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        inverted = self.solution.invertTree(root)
        self.assertEqual(inverted.val, 1)
        self.assertEqual(inverted.left.val, 3)
        self.assertEqual(inverted.right.val, 2)

    def test_larger_tree_level_order(self):
        root = build_tree_from_list([4, 2, 7, 1, 3, 6, 9])
        inverted = self.solution.invertTree(root)
        self.assertEqual(
            to_list_level_order(inverted),
            [4, 7, 2, 9, 6, 3, 1],
        )

    def test_missing_children(self):
        root = build_tree_from_list([1, 2, 3, None, 4, None, 5])
        inverted = self.solution.invertTree(root)
        self.assertEqual(
            to_list_level_order(inverted),
            [1, 3, 2, 5, None, 4],
        )

    def test_double_invert_returns_original(self):
        original = build_tree_from_list([10, 5, 15, None, 7, 12, 20])
        inverted = self.solution.invertTree(original)
        restored = self.solution.invertTree(inverted)
        self.assertEqual(
            to_list_level_order(restored),
            [10, 5, 15, None, 7, 12, 20],
        )


if __name__ == "__main__":
    unittest.main()
