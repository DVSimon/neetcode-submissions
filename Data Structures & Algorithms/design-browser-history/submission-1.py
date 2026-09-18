class BrowserNode:

    def __init__(self, page: str):
        self.prev = None
        self.next = None
        self.page = page

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = BrowserNode(homepage)
        self.tail = BrowserNode("") #Dummy
        self.head.next = self.tail
        self.tail.prev = self.head
        self.current = self.head
        self.forwardVisits = 0
        self.backwardVisits = 0
        

    def visit(self, url: str) -> None:
        newNode = BrowserNode(url)

        newNode.next = self.tail # keep dummy?
        newNode.prev = self.current

        self.current.next = newNode
        self.current = newNode

        self.tail.prev = newNode # make dummy prev as newNode Tail

        self.backwardVisits += 1
        self.forwardVisits = 0
        

    def back(self, steps: int) -> str:
        while steps > 0 and self.current.prev:
            self.current = self.current.prev
            self.forwardVisits += 1
            self.backwardVisits -= 1
            steps -= 1
        return self.current.page
        
        

    def forward(self, steps: int) -> str:
        if steps > self.forwardVisits:
            steps = self.forwardVisits
        while steps > 0 and self.current.next:
            self.current = self.current.next
            self.forwardVisits -= 1
            self.backwardVisits += 1
            steps -= 1
        return self.current.page



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)