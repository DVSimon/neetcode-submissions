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
        self.size = 0
        
    def getPrev(self, index:int) -> ListNode:
        if index <= self.size // 2:
            curr = self.head
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index + 1): 
                curr = curr.prev
        return curr



    def get(self, index: int) -> int:
        # why greater than OR equal?
        if index >= self.size:
            return -1
        node = self.getPrev(index).next
        return node.val
        

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        newNode = ListNode(val)
        prev = self.getPrev(index)

        newNode.next = prev.next
        newNode.prev = prev

        prev.next.prev = newNode
        prev.next = newNode
        self.size += 1

        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        prev = self.getPrev(index)
        node = prev.next

        node.next.prev = prev
        prev.next = node.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)