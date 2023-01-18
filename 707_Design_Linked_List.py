class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1

        if self.head is None:
            return -1

        current = self.head
        for i in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val):
        newnode = Node(val)
        newnode.next = self.head
        self.head = newnode

        self.size += 1

    def addAtTail(self, val):
        current = self.head
        if current is None:
            self.head = Node(val)
        else:
            while current.next is not None:
                current = current.next
            current.next = Node(val)

        self.size += 1

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            newnode = Node(val)
            newnode.next = current.next
            current.next = newnode

            self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return

        current = self.head
        if index == 0:
            self.head = current.next
        else:
            for i in range(index - 1):
                current = current.next
            current.next = current.next.next

        self.size -= 1




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)