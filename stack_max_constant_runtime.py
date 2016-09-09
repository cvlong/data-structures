"""STACK

Design a stack that supports push, pop, peek, and retrieving the maximum element
in O(1) constant time.
"""

class Stack(object):
    """Stack implemented using a list; supports operations in constant time."""

    def __init__(self):
        self.primary_stack = []
        self.max_stack = []

    def peek(self):
        # Return element from top of primary_stack without removing
        return self.primary_stack[len(self.primary_stack) - 1]

    def push(self, value):
        # Add value to top of primary_stack
        self.primary_stack.append(value)

        # If value is greater than current max_value
            # Add value to max_stack
        # Else add current max_value to max_stack
        value_to_append = value
        
        if value < self.max():
            value_to_append = self.max()

        self.max_stack.append(value_to_append)

    def pop(self):
        # Remove element from top of max_stack
        self.max_stack.pop()

        # Remove element from top of primary_stack and return to user
        return self.primary_stack.pop()

    def max(self):
        # If max_stack is not empty, return the elemet from the top of max_stack
        max_value = None

        if len(self.max_stack) > 0:
            max_value = self.max_stack[len(self.max_stack) - 1]
        
        return max_value


if __name__ == '__main__':
    print "Start..."
    example = Stack()
    
    for i in range(6):
        print "Push %i" % i
        example.push(i)

    print "Peek: %i" % example.peek()
    print "Max: %i" % example.max()

    print "Pop"
    example.pop()
    print "Peek: %i" % example.peek()
    print "Max: %i" % example.max()

    print "Push 1"
    example.push(1)
    print "Peek: %i" % example.peek()
    print "Max: %i" % example.max()

    print "Push 100"
    example.push(100)
    print "Peek: %i" % example.peek()
    print "Max: %i" % example.max()

    print "Pop"
    example.pop()
    print "Peek: %i" % example.peek()
    print "Max: %i" % example.max()
