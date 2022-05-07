
class Node:
    def __init__(self, val) -> None:
        """
        """
        self.val = val
        self.leftChild = None
        self.rightChild = None
        self.count = 1

    def __str__(self) -> str:
        return str(self.val) + '(' + str(self.count) + ')'


class BinarySearchTree:
    def __init__(self, root) -> None:
        """
        """
        self.root = root

    def printTree(self) -> None:
        self.printNode(self.root)

    def printNode(self, node, level=0) -> None:
        if node != None:
            index = 0
            spaceString = ""
            while index <= 4*level:
                spaceString += "  "
                index += 1
            nextLevel = level + 1
            self.printNode(node.rightChild, nextLevel)
            print(spaceString + '-> ' + str(node))
            self.printNode(node.leftChild, nextLevel)

    def search(self, target) -> Node:
        """
        """
        node = self.root
        while node is not None and node.val is not target:
            if target > node.val:
                node = node.rightChild
            else:
                node = node.leftChild
        return node

    def insert(self, nodeToInsert) -> None:
        """
        """
        node = self.root
        if node is None:
            self.root = nodeToInsert
        else:
            while node is not nodeToInsert:
                if nodeToInsert.val == node.val:
                    node.count += 1
                    node = nodeToInsert
                elif nodeToInsert.val < node.val:
                    if node.leftChild is None:
                        node.leftChild = nodeToInsert
                    node = node.leftChild
                else:
                    if node.rightChild is None:
                        node.rightChild = nodeToInsert
                    node = node.rightChild

    def preorderTraversal(self, node) -> None:
        if node is not None:
            print(node, end=" ")
            self.preorderTraversal(node.leftChild)
            self.preorderTraversal(node.rightChild)

    def postorderTraversal(self, node) -> None:
        if node is not None:
            self.postorderTraversal(node.leftChild)
            self.postorderTraversal(node.rightChild)
            print(node, end=" ")

    def inorderTraversal(self, node) -> None:
        if node is not None:
            self.inorderTraversal(node.leftChild)
            print(node, end=" ")
            self.inorderTraversal(node.rightChild)


bst = BinarySearchTree(Node(10))
bst.insert(Node(5))
bst.insert(Node(11))
bst.insert(Node(13))
bst.insert(Node(12))
bst.insert(Node(10))
bst.insert(Node(9))
bst.printTree()
print(bst.search(9))
print(bst.search(23))
print(bst.search(5))
bst.inorderTraversal(bst.root)
