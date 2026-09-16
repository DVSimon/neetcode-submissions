class MinStack:

    def __init__(self):
        self.arr = []
        self.minimum = []
        

    def push(self, val: int) -> None:
        if self.minimum:
            self.minimum.append(min(self.minimum[-1], val))
        else:
            self.minimum.append(val)

        self.arr.append(val)
        

    def pop(self) -> None:
        del self.arr[-1]
        del self.minimum[-1]
        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.minimum[-1]
