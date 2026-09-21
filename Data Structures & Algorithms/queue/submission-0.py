class ListNode:

    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        # self.head = ListNode(-1) # Dummy
        # self.tail = self.head
        self.head = ListNode(-1)
        self.tail = ListNode(-1)

        self.head.next  = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        if self.head.next == self.tail:
            return True
        else:
            return False
        

    def append(self, value: int) -> None:
        newNode = ListNode(value)

        newNode.prev = self.tail.prev
        newNode.next = self.tail

        self.tail.prev.next = newNode
        self.tail.prev = newNode
            
        

    def appendleft(self, value: int) -> None:
        newNode = ListNode(value)

        newNode.next = self.head.next
        newNode.prev = self.head

        self.head.next.prev = newNode
        self.head.next = newNode
  

    def pop(self) -> int:
        if self.tail.prev == self.head:
            return -1
        else:
            tempNode = self.tail.prev
            self.tail.prev.prev.next = self.tail
            self.tail.prev = self.tail.prev.prev
            return tempNode.value


        

    def popleft(self) -> int:
        if self.head.next == self.tail:
            return -1
        else:
            tempNode = self.head.next
            self.head.next.next.prev = self.head
            self.head.next = self.head.next.next
            return tempNode.value
            