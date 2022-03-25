class Stack:
    """ Python3 implementation of a simple stack"""

    def __init__(self, size) -> None:
        """ Initializes a stack object.

        Args: 
            self(object) : Current instance of the class.
            size(int) : Total size of the stack.
        """
        self.stack = []
        self.capacity = size

    def push(self, item) -> None:
        """ Pushes an item to the stop of the stack.

        Args:
            self(object) : Current instance of the class.
            item(object) : Item to be pushed to stop of the stack.
        """
        if self.stack.__len__() < self.capacity:
            self.stack.append(item)

    def pop(self) -> object:
        """ Pops an item from the top of the stack.

        Args:
            self(object) : Current instance of the class.
        Returns:
            object: The item being popped off the stack."""
        if self.stack.__len__() > 0:
            return self.stack.pop()

    def isStackEmpty(self) -> bool:
        """ Returns true if the stack is empty. False if not

        Args:
            self(object) : Current instance of the class.
        Returns:
            bool : True if stack is empty, false if not"""
        if self.stack.__len__() == 0:
            return True

    def isStackFull(self) -> bool:
        """ Returns true if the stack is full. False if not

    Args:
        self(object) : Current instance of the class.
    Returns:
        bool : True if stack is full, false if not"""
        if self.stack.__len__() == self.capacity:
            return True

    def printStack(self) -> None:
        """ Prints the current stack.

        Args:
            self(object) : Current instance of class.
        """
        print(self.stack.__str__())


stack = Stack(5)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.printStack()
print('Is stack full:', stack.isStackFull())
print('Removing from stack', stack.pop())
print('Removing from stack', stack.pop())
print('Is stack full:', stack.isStackFull())
stack.printStack()
stack.push(10)
stack.printStack()
print('Removing from stack', stack.pop())
print('Removing from stack', stack.pop())
print('Removing from stack', stack.pop())
print('Removing from stack', stack.pop())
print('Removing from stack', stack.pop())
print('Is stack empty:', stack.isStackEmpty())
