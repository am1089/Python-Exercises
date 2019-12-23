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
                        print(temp.data, '->', end = "", sep = "")
                        temp = temp.next
                print('None')

        # Add node to end of the list
        def addNode(self, node):
                if not self.head:
                        self.head = node
                        return
                temp = self.head
                while (temp and temp.next):
                        temp = temp.next
                temp.next = node
                node.next = None

        # Count the number of times a given number occurs in the linked list
        def search(self, look_for):
                current = self.head
                count = 0
                while (current is not None):
                        if current.data == look_for:
                                count += 1
                        current = current.next
                print(look_for, "was in the linked list", count, "times")
                return count

        # Sort the elements in the linked list
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

        def deleteNode(self, num):
                temp = self.head
                if temp is not None:
                        # Check if head node is num
                        if temp.data == num:
                                self.head = temp.next
                                temp = None
                                print(num, "was deleted from the linked list")
                                return
                        
                        # Search for the node to be deleted
                        while (temp is not None):
                                if temp.data == num:
                                        print(num, "was deleted from the linked list")
                                        break
                                prev = temp
                                temp = temp.next
                                
                        # If num isn't present in linked list
                        if temp == None:
                                print(num, "was not in the linked list")
                                return
                        
                        # Unlink node from linked list
                        prev.next = temp.next
                        temp = None
                        
        def inverse(self):
                prev = None
                current = self.head
                while (current is not None):
                        next = current.next
                        current.next = prev
                        prev = current
                        current = next
                self.head = prev
                                        

List = LinkedList()

#List.addSortedNode(Node(17))
#List.addSortedNode(Node(42))
#List.addSortedNode(Node(50))
#List.addSortedNode(Node(33))
#List.addSortedNode(Node(24))

List.addNode(Node(34))
List.addNode(Node(1))
List.addNode(Node(20))
List.addNode(Node(12))
List.printList()

List.inverse()
List.printList()

#List.deleteNode(20)
#List.deleteNode(2)
#List.printList()

#List.search(12)
