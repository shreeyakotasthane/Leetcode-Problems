class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL():
    def __init__(self):
        self.head = None

    def printList(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next

    def insertBeginning(self):
        newNode = ListNode("Sun")
        newNode.next = list.head
        list.head = newNode
    
    def insertEnd(self):
        

list = SLL()
list.head = ListNode("Mon")
n1 = list.head.next = ListNode("Tue")
n2 = n1.next = ListNode("Wed")
print(n1.next)
list.insertBeginning()
list.printList()