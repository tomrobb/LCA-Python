class Node:

    # Constructor to create a new tree node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# function that returns the pointer to the LCA of two given nodes
# assumes n1 and n2 are present in the tree

class BinaryTree:

    def __init__(self):
        self.root = None

    def findNode(self, key):
        return self.findNode2(self.root, key)

    def findNode2(self, node, key):
        # when node = null
        if node is None or node.key == key:
            return node

        # when key > node
        if key > node.key:
            return self.findNode2(node.right, key)

        # when key < node
        return self.findNode2(node.left, key)

    def addNode(self, key):
        self.root = self.addNode2(self.root, key)


    def addNode2(self, node, key):
        if node is None:
            node = Node(key)
            return node

        if key < node.key:
            node.left = self.addNode2(node.left, key)
        else:
            node.right = self.addNode2(node.right, key)

        return node


    def findLCA(self, n1, n2):
        return self.findLCA2(self.root, n1, n2)

    def findLCA2(self, node, n1, n2):
        # Return None if tree is empty
        if node is None:
            return None

        # If both n1 and n2 are smaller than root
        if node.key > n1 and node.key > n2:
            return self.findLCA2(node.left, n1, n2)

        # If both n1 and n2 are greater than root
        if node.key < n1 and node.key < n2:
            return self.findLCA2(node.right, n1, n2)

        # Else return node
        return node


