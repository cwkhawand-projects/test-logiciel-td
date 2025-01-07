class FIFO:
    """A class implementing a FIFO (First-In-First-Out) queue for storing integers."""

    def __init__(self):
        self.queue = []

    def enqueue(self, value: int):
        """Add an integer to the end of the queue."""
        self.queue.append(value)

    def dequeue(self) -> int:
        """Remove and return the integer at the front of the queue."""
        if not self.queue:
            raise IndexError("Dequeue from empty FIFO queue")
        return self.queue.pop(0)

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def peek(self) -> int:
        """Return the integer at the front of the queue without removing it."""
        if not self.queue:
            raise IndexError("Peek from empty FIFO queue")
        return self.queue[0]


class LIFO:
    """A class implementing a LIFO (Last-In-First-Out) stack for storing integers."""

    def __init__(self):
        self.stack = []

    def push(self, value: int):
        """Add an integer to the top of the stack."""
        self.stack.append(value)

    def pop(self) -> int:
        """Remove and return the integer at the top of the stack."""
        if not self.stack:
            raise IndexError("Pop from empty LIFO stack")
        return self.stack.pop()

    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def peek(self) -> int:
        """Return the integer at the top of the stack without removing it."""
        if not self.stack:
            raise IndexError("Peek from empty LIFO stack")
        return self.stack[-1]
