"""QUEUE

- FIFO: first in first out. Enqueue items at the back; dequeue items at the front
  enqueue(item), dequeue(), peek(), is_empty()
- Better to build Queue class using a doubly linked list
"""

class Queue(object):
    """Queue implemented using a list"""

    def __init__(self):
        self._queue = []

    def enqueue(self, item):
        self._queue.append(item)

    def dequeue(self):
        self._queue.pop(0)

    def peek(self):
        return self._queue[0]

    def is_empty(self):
        return not self._queue


"""STACK

- LIFO: last in first out. Push items onto the top; pop items off the top
  push(item), pop(), peek(), is_empty()
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