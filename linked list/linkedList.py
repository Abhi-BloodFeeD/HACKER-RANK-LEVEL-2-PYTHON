class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        # Complete this method
        newNode = Node(data)
        if head == None:
            return newNode

        else:
            thisNode = head
            while (True):
                if thisNode.next == None:
                    break
                thisNode = thisNode.next
            #thisNode = thisNode.next
            thisNode.next = Node(data)
            return head

"""
    def insert(self, head, data):
        # Complete this method
        newNode = Node(data)
        if not head:
            return newNode
        current = head
        while current.next:
            current = current.next
        current.next = newNode
        return head
"""

mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)
