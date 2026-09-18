class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1) # dummy node
        self.tail = ListNode(-1) # dummy node
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next
        while curr != self.tail:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1
        

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)

        newNode.prev = self.head
        newNode.next = self.head.next

        self.head.next.prev = newNode
        self.head.next = newNode

        

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)

        newNode.next = self.tail
        newNode.prev = self.tail.prev

        self.tail.prev.next = newNode
        self.tail.prev = newNode
        

    def addAtIndex(self, index: int, val: int) -> None:
        i = 0
        curr = self.head
        while curr != self.tail:
            if i == index:
                newNode = ListNode(val)
                newNode.next = curr.next
                newNode.prev = curr

                curr.next.prev = newNode
                curr.next = newNode
                return
            curr = curr.next
            i += 1

        

    def deleteAtIndex(self, index: int) -> None:
        i = 0
        curr = self.head.next
        while curr != self.tail:
            if i == index:
                curr.next.prev = curr.prev
                curr.prev.next = curr.next
                return
            curr = curr.next
            i += 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)