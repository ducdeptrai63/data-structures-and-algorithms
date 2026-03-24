import unittest

from n_ary_tree_postorder_traversal import Node
from n_ary_tree_postorder_traversal import Solution


class TestNAryTreePostorderTraversal(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @staticmethod
    def makeNode(val, children=None):
        if children is None:
            children = []
        return Node(val, children)

    def testNoneRootReturnsEmptyList(self):
        res = self.solution.postorder(None)
        self.assertEqual(res, [])

    def testSingleNodeNoChildren(self):
        root = self.makeNode(42, [])
        res = self.solution.postorder(root)
        self.assertEqual(res, [42])

    def testLeetCodeExample(self):
        # Tree:
        #        1
        #     /  |  \
        #    3   2   4
        #   / \
        #  5   6
        n5 = self.makeNode(5)
        n6 = self.makeNode(6)
        n3 = self.makeNode(3, [n5, n6])
        n2 = self.makeNode(2)
        n4 = self.makeNode(4)
        root = self.makeNode(1, [n3, n2, n4])

        res = self.solution.postorder(root)
        self.assertEqual(res, [5, 6, 3, 2, 4, 1])

    def testDeeperIrregularTree(self):
        # Tree:
        #            10
        #     /       |        \
        #    20      30        40
        #  /   \       \      / | \
        # 50   60      70    80 90 100
        #      / \
        #     61  62
        n50 = self.makeNode(50)
        n61 = self.makeNode(61)
        n62 = self.makeNode(62)
        n60 = self.makeNode(60, [n61, n62])
        n20 = self.makeNode(20, [n50, n60])

        n70 = self.makeNode(70)
        n30 = self.makeNode(30, [n70])

        n80 = self.makeNode(80)
        n90 = self.makeNode(90)
        n100 = self.makeNode(100)
        n40 = self.makeNode(40, [n80, n90, n100])

        root = self.makeNode(10, [n20, n30, n40])

        res = self.solution.postorder(root)
        expected = [50, 61, 62, 60, 20, 70, 30, 80, 90, 100, 40, 10]
        self.assertEqual(res, expected)

    def testChildrenListCanContainNoneEntries(self):
        # dfs(None) should be safe because the implementation checks `if not root: return`.
        a = self.makeNode(1)
        b = self.makeNode(2)
        root = self.makeNode(0, [a, None, b])

        res = self.solution.postorder(root)
        self.assertEqual(res, [1, 2, 0])

    def testChildrenIsNoneRaisesTypeError(self):
        # Implementation iterates: `for child in root.children`.
        # If children is None, Python raises TypeError: 'NoneType' object is not iterable.
        root = Node(1, None)
        with self.assertRaises(TypeError):
            self.solution.postorder(root)


if __name__ == '__main__':
    unittest.main()
