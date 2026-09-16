class LinkedList:
    
    def __init__(self):
        self.linkedlist = []
        self.length = 0

    
    def get(self, index: int) -> int:
        if index < self.length:
            return self.linkedlist[index]
        return -1
        

    def insertHead(self, val: int) -> None:
        self.linkedlist.insert(0,val)
        self.length += 1

    def insertTail(self, val: int) -> None:
        self.linkedlist.append(val)
        self.length += 1
        

    def remove(self, index: int) -> bool:
        if index < self.length:
            del self.linkedlist[index]
            self.length -= 1
            return True
        return False

    def getValues(self) -> List[int]:
        return self.linkedlist
        
