class Node:
    """ Python3 simple implementation of Node for a LL"""

    def __str__(self) -> str:
        """ Returns the string representation of Node.

        Args:
            self(object): The current instance of the class.
        Returns:
            string: The string representation of Node.
        """
        return str(self.data)

    def __init__(self, data=None) -> None:
        """ Initializes a Node.
        Args:
            self(object) : Current instance of the object.
            data(object) : Data that is contained within a node. Defaulted to None
        """
        self.data = data
        self.next = None


class LinkedList:
    """ Python3 simple implementation of a linkedlist"""

    def __str__(self) -> str:
        """ Returns string represenation of linkedlist.

        Args: 
            self(object): Current instance of the class.
        Returns:
            string: LinkedList in a string representation.
        """
        string = ''
        node = self.head
        while True:
            string = string + str(node)
            if node is None:
                break
            string = string + ' -> '
            node = node.next
        return string

    def __init__(self) -> None:
        """ Initializes an empty LinkedList

        Args:
            self(object): Current instance of class."""
        self.head = None

    def insert(self, node) -> None:
        """ Inserts node into the head of the Linked list

        Args:
            self(object) : Current instance of class.
            node(object) : Node to be inserted into LinkedList.
        """
        if self.head is not None:
            node.next = self.head
        self.head = node
        self.key = node.data

    def search(self, target) -> list:
        """ Searches LinkedList for a Node and returns pointers to this element.

        Args:
            self(object): Current instance of class.
            target(object): Node to be searched for in LinkedList
        """
        keys = []
        index = 0
        node = self.head
        while node is not None:
            if node.data == target:
                keys.append(index)
            index += 1
            node = node.next
        return keys

    def delete(self, target) -> None:
        """ Deletes element from LinkedList
        Args:
            self(object) : Current instance of class.
            target(object) : Target element to be deleted from LinkedList
        """
        node = self.head
        while node is not None:
            if node.data == target and node is self.head:
                self.head = node.next
                break
            elif node.next is not None:
                if node.next.data == target:
                    if(node.next.next is None):
                        node.next = None
                    else:
                        node.next = node.next.next
            node = node.next


# Test inserting multiple elements
linkedlist = LinkedList()
linkedlist.insert(Node(3))
linkedlist.insert(Node(4))
linkedlist.insert(Node(5))
linkedlist.insert(Node(3))
print(linkedlist)
assert str(linkedlist) == '3 -> 5 -> 4 -> 3 -> None'

# Test searching for all positions 3 exists.
print('3 is at these positions:', linkedlist.search(3))
assert linkedlist.search(3) == [0, 3]

# Test deleting first element 3
linkedlist.delete(3)
print('3 is at these positions:', linkedlist.search(3))
assert linkedlist.search(3) == [2]

# Test deleting all elements
print(linkedlist)
linkedlist.delete(5)
print(linkedlist)
linkedlist.delete(4)
print(linkedlist)
linkedlist.delete(3)
print(linkedlist)
assert str(linkedlist) == 'None'

# Test deleting when linkedlist is empty
linkedlist.delete(2)
print(linkedlist)
assert str(linkedlist) == 'None'

# Testing two head elements that are the same.
linkedlist.insert(Node(3))
linkedlist.insert(Node(3))
linkedlist.insert(Node(4))
linkedlist.insert(Node(3))
linkedlist.delete(Node(3))
print(linkedlist)
assert str(linkedlist) == '3 -> 4 -> 3 -> 3 -> None'
