"""QUEUES

- First in, first out (FIFO)
- Enqueue items at the back; dequeue items at the front
- Runtime:
    - Add-R: O(1)
    - Pop-L: O(n)
- Common methods: enqueue(item), dequeue(), peek(), is_empty()
- More time efficient to build Queue class using a doubly linked list (but that
trades runtime for space)

"""

class Queue(object):
    """Queue implemented using a list."""

    def __init__(self):
        self._queue = []

    # add items to the end of the list: O(1)
    def enqueue(self, item):
        self._queue.append(item)

    # pop items from the front of the list: O(n)
    def dequeue(self):
        self._queue.pop(0)

    def peek(self):
        return self._queue[0]

    def is_empty(self):
        return not self._queue


"""STACKS

- Last in, first out (LIFO)
- Push items onto the top; pop items off the top
- Runtime:
    - Add-R: O(n)
    - Pop-R: O(n)
- Common methods: push(item), pop(), peek(), is_empty()

"""

class Stack(object):
    """Stack implemented using a list."""

    def __init__(self, lst):
        self._stack = lst
        self._length = len(lst)

    def __repr__(self):
        if not self._stack:
            return '<Stack empty>'
        else:
            return '<Stack next item: %s; length: %d>' % (self._stack[-1],
                                                          self._length)

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        self._stack.pop()

    def peek(self):
        return self._stack[-1]

    def is_empty(self):
        return not self._stack

    def length(self):
        return self._length


fruits = Stack(['apple', 'berry', 'cherry'])
fruits.push('durian')

print fruits
print fruits.length()
print fruits.peek()