"""TREE

- Children has to be an empty list. Note: use None, not [] for the default value
  when instantiating the Node object. Don't use a mutable default argument
  because then the empty list is made once and shared by all calls. By using a
  non-mutable argument, we check for a value and assign a new empty list each
  time a node is instantiated

- Depth first search (DFS) uses a stack to track nodes to visit
- Breadth first search (BFS) uses a queue to track nodes to visit. Better for finding
  the highest ranking element, since all siblings checked before any descendents
"""

class Node(object):
    """Node in a tree."""

    def __init__(self, data, children=None):
        children = children or []
        assert isinstance(children, list)
        self.data = data
        self.children = children

    def __repr__(self):
        return '<Node: %s>' % self.data

# Ex1
# sharon = Node('Sharon')
# sharon.children.append(Node('Angie'))
# sharon.children.append(Node('Stefan'))
# print sharon.children

# Ex2
# sharon = Node('Sharon', [Node('Angie'), Node('Stefan')])
# print sharon.children

    def depth_first_search(self, value):
        """Return node object using a depth first search.

        Uses a STACK to keep track of nodes in to_visit. Starts at the root node,
        then search its children. Search the children of the current node (and its
        children, etc.) before the next sibling and the sibling's children.
        Effectively goes to the end of the rightmost branch before moving on to
        the next child. 
        """

        to_visit = [self] #keep a list of nodes to visit

        while to_visit: #while the list still contains nodes to check (otherwise implicitly returns None)
            node = to_visit.pop() #uses a stack (LIFO)

            if node.data == value:
                return node #WINS FAST

            to_visit.extend(node.children) 

    def recursive_depth_first_search(self, value):
        ###


    def breadth_first_search(self, value):
        """Return node object using a breadth first search; finds highest ranking value.

        Uses a QUEUE to keep track of nodes in to_visit. Starts at the root node,
        then search its children. Search all the siblings of the current node
        before checking its children (use a queue since the higher ranking elements
        get appended first). Effectively searches each level of siblings from
        left to right before going to any of their descendents in the same order.
        """

        to_visit = [self]

        while to_visit:
            node = to_visit.pop(0) #uses a queue (FIFO)

            if node.data == value:
                return node

            to_visit.extend(node.children)

    def recursive_breadth_first_search(self, value):
        ###


class Tree(object):
    """Tree."""

    def __init__(self, root):
        self.root = root

    def __repr__(self):
        return '<Tree root: %s>' % self.root

    def find_node(self, value):
        """Find a node by value.

        Delegate this method onto the root node, so the search starts on the root
        and can be used on the entire tree.
        """

        return self.root.depth_first_search(value)


class ReverseNode(object):
    """Node in a tree that points to its parent."""

    def __init__(self, parent=None):
        self.parent = parent


class BidirectionalNode(object):
    """Node in a tree that points to both its parent and children."""

    def __init__(self, parent=None, children=None):
        self.parent = parent
        self.children = children or []