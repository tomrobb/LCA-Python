from unittest import TestCase
from LCA import *


class Test(TestCase):
    def test_find_lca(self):
        # Testing with the following binary tree:
        #                              1
        #                         /         \
        #                        2            3
        #                    /       \     /     \
        #                  4         5    6        7

        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)

        self.assertEqual(3, findLCA(root, 6, 7).key)
        self.assertEqual(2, findLCA(root, 4, 5).key)
        self.assertEqual(1, findLCA(root, 2, 6).key)
        self.assertEqual(3, findLCA(root, 3, 7).key)

