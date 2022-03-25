class Queue:
    """Python3 Implementation of a Queue"""

    def __init__(self, size) -> None:
        """Initializes a queue object

        Args:
            self (object): Current instance of the class.
            size (int): The capacity of the queue."""
        self.queue = []
        self.capacity = size

    def enqueue(self, item) -> None:
        """ Enqueues item to the queue if there is space.

        Args:
            self(object): Current instance of the class.
            item(object): The item to be added to the queue.
        """
        if self.queue.__len__() < self.capacity:
            self.queue.append(item)

    def dequeue(self) -> object:
        """ Dequeues and item from the queue if it has items.

        Args:
            self(object): Current instance of the class.
        Returns:
            object: First object in the queue.
        """
        if self.queue.__len__() > 0:
            return self.queue.pop(0)
        else:
            return None

    def isEmpty(self) -> bool:
        """ Checks if the queue is empty.

        Args:
            self(object): Current instance of the class.
        Returns:
            bool: True if the queue is empty, false is it is not.
        """
        if self.queue.__len__ == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        """ Checks if the queue is full.

        Args:
            self(object): Current instance of the class.
        Returns:
            bool: True if the queue is full, false if it is not.
        """
        if self.queue.__len__ == self.capacity:
            return True
        else:
            return False

    def printQueue(self) -> str:
        """ Prints the queue to the console.

        Args:
            self(object): Current instance of the class.
        """
        print(self.queue.__str__())


queue = Queue(2)
queue.enqueue(1)
queue.enqueue(2)
queue.printQueue()
queue.dequeue()
queue.enqueue(1)
queue.enqueue(3)
queue.printQueue()
queue.dequeue()
queue.dequeue()
queue.enqueue(3)
queue.printQueue()
