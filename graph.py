"""GRAPH

- Nodes have 0+ adjacencies; cyclic or acyclic; relationships are directed or 
  non-directed. Whereaas trees are directed, acyclic graphs
- Forests are a collection of directed, acyclic graphs without a single root
  node
"""

class Node(object):
    """Node in a graph."""

    def __init__(self, data, adjacency=None):
        adjacency = adjacency or set()
        assert isinstance(adjacency, set)
        self.data = data
        self.adjacency = adjacency

    def __repr__(self, data):
        return '<Node: %s>' % self.data


class Graph(object):
    """Graph."""

    def __init__(self):
        self.nodes = set() #create an empty graph with no nodes

    def __repr__(self):
        return '<Graph node: %s>' % [n.data for n in self.nodes]

    def add_node(self, data):
        """Add data to graph node."""

        self.nodes.add(data)

    def set_adjacency(self, data1, data2):
        """Set two nodes as adjacent.

        Make this method on the Graph class, rather than the Node class, so you
        can execute this method once, instead of once on each node.
        """

        data1.adjacency.add(data2)
        data2.adjacency.add(data1)