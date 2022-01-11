# Stacks

import link

class Stack:
    """Stack data structure.
    attributes:
    - head: first Link in stack, None if stack is empty"""
    def __init__(self):
        """Initialises an empty stack."""
        self.head = None

    def is_empty(self):
        """Checks if the stack is empty."""
        return self.head is None

    def top(self):
        """Returns the element at the top of the stack without removing it."""
        if self.is_empty():
            raise ValueError("top of empty stack")
        else:
            return self.head.first

    def push(self, val):
        """Pushes val onto the top of the stack."""
        if self.is_empty():
            self.head = link.Link(val)
        else:
            self.head = link.Link(val, self.head)

    def pop(self):
        """Removes the element at the top of the stack and returns it."""
        if self.is_empty():
            raise ValueError('pop from empty stack')
        else:
            val = self.head.first
            if link.empty(self.head.rest):
                self.head = None
            else:
                self.head = self.head.rest
            return val

    def __str__(self):
        if self.is_empty():
            return 'empty stack'
        else:
            res = 'stack:'
            node = self.head
            while not link.empty(node):
                res += ' ' + str(node.first)
                node = node.rest
            return res
