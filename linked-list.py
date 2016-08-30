"""LINKED LIST

- Group of nodes in a sequence; each node has a value (.data) & pointer (.next);
  the linked list object has a head attribute
"""

class Node(object):
    """Node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return '<Node value: %d>' % self.data

new_node = Node(5)
print new_node


class LinkedList(object):
    """Linked list."""

    def __init__(self):
        self.head = None

    def print_list(self):
        """Print all items in the linked list."""

        current = self.head

        while current is not None:
            
            print current.data
            current = current.next

    def find_node(self, data):
        """Find a node in a linked list."""

        current = self.head

        while current is not None:
            if current.data == data:
                return True

            current = current.next

        return False

    def add_node(self, data):
        """Add a node to the end of a linked list without a tail."""

        new_node = Node(data) #instantiate a new instance of the Node class

        if self.head is None:
            self.head = new_node
        
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

    def remove_by_value(self, value):
        """Remove a node by value without tracking previous node."""

        # If list has a head (AKA not empty) and head has the value, make 2nd item the new head
        if self.head and self.head.data == value:
            self.head = self.head.next
            return

        current = self.head

        while current.next is not None:  
            
            if current.next.data == value:
                current.next = current.next.next
                return

            else:
                current = current.next

    def remove_by_value2(self, value):
        """Remove a node by value by tracking the previous node."""

        current = self.head
        prev = None

        while current is not None:

            if current.data == value:
                if prev is None:                
                    self.head = current.next
                else:
                    prev.next = current.next
                return

            else:
                prev = current
                current = current.next

    def remove_by_index(self, index):

        i = 0
        node = self.head
        prev = None

        while (node is not None) and (i < index):
            prev = node
            node = node.next
            i += 1

        if prev is None:
            self.head = node.next
        else:
            prev.next = node.next


my_ll = LinkedList()


"""DOUBLY LINKED LIST"""

class Node(object):
    """Node in a doubly linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList(object):
    """Doubly linked list."""

    def __init__(self):
        #####