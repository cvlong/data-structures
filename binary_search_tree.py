"""BINARY SEARCH TREE

- Tree made of nodes; each node has a left and right child (rather than children list)
- Each step reduces the number of options by half
- For n nodes, max runtime is O(log n)
- Won't get runtime advantages if binary tree is badly balanced - then it's just
  like a linked list. Check the longest branch and shortest branch to make sure
  they're not more than one level off.
"""

class BinaryNode(object):
    """Binary tree node."""

    def __init__(self, data, left=None, right=None):
        assert left is None or isinstance(left, BinaryNode) #has to be a binary node
        assert right is None or isinstance(right, BinaryNode)

        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return '<BinaryNode: %s>' % self.data

    def find_node(self, value):
        """Return binary node with particular value."""

        node = self #initialize node to be self

        while node: #otherwise function will implicitly return None
            
            # print 'checking', node.data

            if node.data == value:
                return node

            elif value < node.data:
                node = node.left

            elif value > node.data:
                node = node.right