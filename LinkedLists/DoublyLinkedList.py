class Node:
    """Node for DoublyLinked List"""

    def __str__(self) -> str:
        """ Returns the string representation of Node.

        Args:
            self(object): The current instance of the class.
        Returns:
            string: The string representation of Node.
        """
        return str(self.data)

    def __init__(self, data) -> None:
        """ Creates a node with key of data

        Args:
            data(object): Data to be used as node key
        """
        self.data = data
        self.prev = None
        self.next = None


class DoubleLinkedList:
    """Python 3 simple implementation of doubly linked list"""

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
        """
        self.head = None

    def search(self, item) -> Node:
        """ Searches LinkedList for first element that contains key item

        Args:
            item(object): The key to be searched for in linkedlist
        Returns:
            Node: The first node in the list that contains the key.
        """
        node = self.head
        while node is not None and node.data is not item:
            node = node.next
        return node

    def insert(self, item) -> None:
        """ Inserts node as the head of the linkedlist

        Args: 
            item(object): Node to be added to the linkedlist.
        """
        item.next = self.head
        if self.head is not None:
            self.head.prev = item
        self.head = item
        item.prev = None

    def delete(self, item) -> None:
        """ Deletes the first instance of the Node from the linkedlist.

        Args: 
            item(object): Key to be searched and used to obtain node to delete from linkedlist.
        """
        node = self.search(item)
        if node is not None:
            if node.prev is not None:
                node.prev.next = node.next
            else:
                self.head = node.next
            if node.next is not None:
                node.next.prev = node.prev


# Test inserting multiple elements
linkedlist = DoubleLinkedList()
linkedlist.insert(Node(3))
linkedlist.insert(Node(4))
linkedlist.insert(Node(5))
linkedlist.insert(Node(3))
print(linkedlist)
assert str(linkedlist) == '3 -> 5 -> 4 -> 3 -> None'

# Test searching for all positions 3 exists.
print('The first element of 3 is at:', id(linkedlist.search(3)))
assert id(linkedlist.search(3)) == id(linkedlist.head)

# Test deleting first element 3
linkedlist.delete(3)
print('The first element of 3 is at:', id(linkedlist.search(3)))
assert id(linkedlist.search(3)) == id(linkedlist.head.next.next)

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

# Testing negative numbers
linkedlist.insert(Node(-1))
print(linkedlist)
assert str(linkedlist) == '-1 -> 3 -> 4 -> 3 -> 3 -> None'
