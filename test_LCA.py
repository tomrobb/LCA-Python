from unittest import TestCase

import LCA
from LCA import *


class Test(TestCase):

    def testNode(self):
        node = LCA.Node(1)

        self.assertEqual(1, node.key)

    def testBinaryTree(self):
        tree = LCA.BinaryTree()

        self.assertEqual(None, tree.root)

    def testFindNodeKeyNull(self):
        tree = LCA.BinaryTree()

        self.assertEqual(None, tree.findNode(10))

    def testFindNodeEqualRoot(self):
        tree = LCA.BinaryTree()
        tree.addNode(10)

        self.assertEqual(10, tree.findNode(10).key)

    def testFindNodeBiggerRoot(self):
        tree = LCA.BinaryTree()
        tree.addNode(10)
        tree.addNode(20)

        self.assertEqual(20, tree.findNode(20).key)

    def testFindNodeSmallerRoot(self):
        tree = LCA.BinaryTree()
        tree.addNode(20)
        tree.addNode(10)

        self.assertEqual(10, tree.findNode(10).key)

    def testLeft(self):
        tree = LCA.BinaryTree()
        tree.addNode(10)
        tree.addNode(5)

        self.assertEqual(tree.findNode(5), tree.findNode(10).left)

    def testRight(self):
        tree = LCA.BinaryTree()
        tree.addNode(10)
        tree.addNode(15)

        self.assertEqual(tree.findNode(15), tree.findNode(10).right)

    def testLCANull(self):
        tree = LCA.BinaryTree()
        self.assertEqual(None, tree.findLCA(10,20))

    def testLCASimple(self):
        tree = LCA.BinaryTree()
        tree.addNode(20)
        tree.addNode(10)
        tree.addNode(30)

        self.assertEqual(tree.findNode(20), tree.findLCA(10,30))

    def testLCA(self):
        # Testing with the following binary tree:
        #                              35
        #                         /         \
        #                        20           50
        #                    /       \     /     \
        #                  10         30   40     70
        tree = LCA.BinaryTree()
        tree.addNode(35)
        tree.addNode(20)
        tree.addNode(50)
        tree.addNode(10)
        tree.addNode(30)
        tree.addNode(40)
        tree.addNode(70)
        self.assertEqual(tree.findNode(20), tree.findLCA(10, 30))
        self.assertEqual(tree.findNode(50), tree.findLCA(40, 70))
        self.assertEqual(tree.findNode(20), tree.findLCA(10, 20))
        self.assertEqual(tree.findNode(50), tree.findLCA(50, 70))
        self.assertEqual(tree.findNode(35), tree.findLCA(10, 70))



