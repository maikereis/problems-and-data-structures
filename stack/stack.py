"""Implements a stack data structure in python."""


class Stack:
    def __init__(self):
        """Initializes Stack class.
        Attributes:
            name (list): The primitive data structure used as base.
        """
        self.items = []

    def is_empty(self):
        """Verify is the Stack is empty."""
        return self.items == []

    def push(self, item):
        """Add a new item on top of the Stack."""
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        """Return the element on top of the Stack."""
        return self.items[len(self.items) - 1]

    def size(self):
        """Return the stack size."""
        return len(self.items)
