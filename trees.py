
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(node):
    if node is None: return
    inorder(node.left)
    print(node.val)
    inorder(node.right)


def preorder(node):
    if node is None: return
    print(node.val)
    preorder(node.left)
    preorder(node.right)


def postorder(node):
    if node is None: return
    postorder(node.left)
    postorder(node.right)
    print(node.val)


# Tree manually created
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)
root.left.left.left = Node(6)
root.left.left.right = Node(7)


def find_height(node):
    """Finds the height of the tree by dividing the problem into smaller subproblems.

    Logic: height of tree = height of tallest subtree + 1
    Rationale: Tallest subtree + root => same height as the original tree

    Key learning point:
    Define the problem and determine what the solution is. 
    Afterwards, think of the answer in terms of smaller subproblems (recursive thinking)
    """
    if node is None: return 0
    lheight = find_height(node.left)
    rheight = find_height(node.right)

    # The height of a tree is equal to the height of its tallest subtree + 1
    # This is because the subtree + root has the same height
    return 1 + max(lheight, rheight)


def node_count(node):
    if node is None: return 0
    lcount = node_count(node.left)
    rcount = node_count(node.right)

    return 1 + lcount + rcount


def path_sum(target, node):
    if node is None: return False
    target -= node.val
    if node.left is None and node.right is None:
        return target == 0
    return path_sum(target, node.left) or path_sum(target, node.right)


# testing
if __name__ == '__main__':
    print(path_sum(13, root))