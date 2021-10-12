class Node:

    # Constructor to create a new tree node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# function that returns the pointer to the LCA of two given nodes
# assumes n1 and n2 are present in the tree

def findLCA(root, n1, n2):
    if root is None:
        return None

    # If either n1 or n2 matches with root's key, report
    #  the presence by returning root (Note that if a key is
    #  ancestor of other, then the ancestor key becomes LCA
    if root.key == n1 or root.key == n2:
        return root

    # Look for keys in left and right subtrees
    left_lca = findLCA(root.left, n1, n2)
    right_lca = findLCA(root.right, n1, n2)

    # If both of the above calls return Non-NULL, then one key
    # is present in once subtree and other is present in other,
    # So this node is the LCA
    if left_lca and right_lca:
        return root

    # Otherwise check if left subtree or right subtree is LCA
    return left_lca if left_lca is not None else right_lca


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
print("The LCA of 6 and 7 = ", findLCA(root, 6, 7).key)  # 3
print("The LCA of 4 and 5 = ", findLCA(root, 4, 5).key)  # 2
print("The LCA of 2 and 6 = ", findLCA(root, 2, 6).key)  # 1
print("The LCA of 3 and 7 = ", findLCA(root, 3, 7).key)  # 3
