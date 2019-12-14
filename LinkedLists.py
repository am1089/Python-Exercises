# Linked Lists

class Node:
        def __init__(self, data):
                self.data = data
                self.next = None # Initialize next as null
                return None

class LinkedList:
        def __init__(self):
                self.head = None

        # Prints contents of linked list
        def printList(self):
                temp = self.head
                while (temp):
                        print(temp.data)
                        temp = temp.next

        # Add note to end of the list
        def addNode(self, node):
                if not self.head:
                        self.head = node
                        return
                temp = self.head
                while (temp and temp.next):
                        temp = temp.next
                temp.next = node
                node.next = None

        # Add nodes in ascending order
        # Assume that list is already in order
        def addSortedNode(self, node):
                if not self.head:
                        self.head = node
                        return
                temp = self.head
                while (temp and node.data > temp.data):
                        prev = temp
                        temp = temp.next
                if temp:
                        prev.next = node
                        node.next = temp
                else:
                        prev.next = node  

List = LinkedList()

List.addSortedNode(Node(17))
List.addSortedNode(Node(42))
List.addSortedNode(Node(50))
List.addSortedNode(Node(33))
List.addSortedNode(Node(24))

List.printList()
