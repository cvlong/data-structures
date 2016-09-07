"""GRAPH

- Nodes have 0+ adjacencies; cyclic or acyclic; relationships are directed or 
  non-directed. Whereaas trees are directed, acyclic graphs
- Forests are a collection of directed, acyclic graphs without a single root
  node
"""

from queue_and_stack import Queue

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


#Graph implementation showing relationships among friends

class PersonNode(object):
    """Node in a graph representing a person."""

    def __init__(self, name, adjacency=None):
        adjacency = adjacency or set()
        assert isinstance (adjacency, set)
        self.name = name
        self.adjacency = adjacency

    def __repr__(self):
        return '<PersonNode: %s>' % self.name


class FriendGraph(object):
    """Graph showing relationships among friends."""

    def __init__(self):
        self.nodes = set() #create an empty graph

    def __repr__(self):
        return '<FriendGraph: %s>' % [n.name for n in self.nodes]

    def add_person(self, person):
        """Add person to friend graph."""

        self.nodes.add(person)

    def set_friends(self, person1, person2):
        """Set two people as friends."""

        person1.adjacency.add(person2)
        person2.adjacency.add(person1)

    def add_people(self, people_lst):
        """Add a list of people to friend graph."""

        for person in people_lst:
            self.add_person(person)

    def check_friendship(self, person1, person2):
        """Check whether two people are connected by navigating through adjacencies.

        Use a queue to perform a breadth first search by adding adjacencies to
        the end of the list, and popping elements off of the front to evaluate.
        """

        possible_nodes = Queue()
        seen = set()
        possible_nodes.enqueue(person1)
        seen.add(person1)

        while not possible_nodes.is_empty(): #while the queue has items
            
            person = possible_nodes.dequeue()
            print 'checking', person
            
            if person is person2:
                return True
            
            # FIX THIS PART
            # else:
            #     for friend in person1.adjacency - seen:
            #         possible_nodes.enqueue(friend)
            #         seen.add(friend)
            #         print 'added to queue: ', friend
            
            return False


if __name__ == '__main__':

    # Instantiate person nodes
    harry = PersonNode("Harry")
    hermione = PersonNode("Hermione")
    ron = PersonNode("Ron")
    neville = PersonNode("Neville")
    trevor = PersonNode("Trevor")
    fred = PersonNode("Fred")
    draco = PersonNode("Draco")
    crabbe = PersonNode("Crabbe")
    goyle = PersonNode("Goyle")

    # Instantiate a new graph
    friends = FriendGraph()
    friends.add_people([harry, hermione, ron, neville, fred, draco, crabbe, goyle])

    # Set edges between friend nodes
    friends.set_friends(harry, hermione)
    friends.set_friends(harry, ron)
    friends.set_friends(harry, neville)
    friends.set_friends(hermione, ron)
    friends.set_friends(neville, hermione)
    friends.set_friends(neville, trevor)
    friends.set_friends(ron, fred)
    friends.set_friends(draco, crabbe)
    friends.set_friends(draco, goyle)

    print friends.check_friendship(ron, trevor)