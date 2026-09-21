# easy solution is interating through students ; how would we get the end node?

# create a queue for the students
# I guess for sandwiches as well.. But we only need to know head/tail really, maybe a LL

class ListNode:

    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None

class studentQueue:
    
    def __init__(self, nodes: list[int]):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next  = self.tail
        self.tail.prev = self.head
        for node in nodes:
            self.append(node)

    def checkStudents(self, value: int) -> bool:
        # if the pref matches
        if self.head.next.value == value:
            self.popleft()
            return True
        # if it doesnt match then shuffle to end
        else:
            tempNodeVal = self.popleft()
            self.append(tempNodeVal)
            return False


    def append(self, value: int) -> None:
        newNode = ListNode(value)

        newNode.prev = self.tail.prev
        newNode.next = self.tail

        self.tail.prev.next = newNode
        self.tail.prev = newNode

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
            

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        newStudents = studentQueue(students)
        res = len(students)
        count = 0
        while sandwiches and count < res:
            if newStudents.checkStudents(sandwiches[0]):
                sandwiches.pop(0)
                res -= 1
                count = 0
            else: 
                count += 1
        return res

        