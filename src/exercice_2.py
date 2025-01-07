class FIFO:
    """A class implementing a FIFO (First-In-First-Out) queue for storing integers."""

    def __init__(self):
        self.queue = []

    def enqueue(self, value: int):
        """Add an integer to the end of the queue."""
        pass

    def dequeue(self) -> int:
        """Remove and return the integer at the front of the queue."""
        pass

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        pass

    def peek(self) -> int:
        """Return the integer at the front of the queue without removing it."""
        pass


class LIFO:
    """A class implementing a LIFO (Last-In-First-Out) stack for storing integers."""

    def __init__(self):
        self.stack = []

    def push(self, value: int):
        """Add an integer to the top of the stack."""
        pass

    def pop(self) -> int:
        """Remove and return the integer at the top of the stack."""
        pass

    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        pass

    def peek(self) -> int:
        """Return the integer at the top of the stack without removing it."""
        pass
