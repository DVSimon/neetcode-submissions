class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.maxHeap = [0]
        for num in nums:
            self.push(num)
        # First things first we need to sort the nums..

    def push(self, val):
        # We use this to push a new value into maxheap
        # We also use for initializing max heap
        self.maxHeap.append(val)
        i = len(self.maxHeap) - 1

        # 0'th element is null in maxHeap.
        while i > 1 and self.maxHeap[i] < self.maxHeap[i // 2]:
            # temp = self.maxHeap[i]
            # self.maxHeap[i] = self.maxHeap[i//2]
            # self.maxHeap[i//2] = temp
            # i = i//2 
            self.maxHeap[i], self.maxHeap[i//2] = self.maxHeap[i//2], self.maxHeap[i]
            i = i//2
        # we've added the new element in
        # we need to pop it if len(maxHeap) > k
        if len(self.maxHeap) - 1 > self.k:
            self.pop()

    def pop(self):
        # We need to remove top by making it = to bottom then removing bottom element
        # After that we bubble that element down the tree to its spot
        
        # First handle two cases where empty and only size 1
        # case 1 only 0(dummy) element
        if len(self.maxHeap) <= 1:
            return
        # case 2 only 1 element just return pop
        if len(self.maxHeap) == 2:
            return self.maxHeap.pop()

        # otherwise handle the hard case...
        i = 1
        # delete top element by replacement from bottom
        self.maxHeap[1] = self.maxHeap[len(self.maxHeap) - 1]
        # remove bottom element
        self.maxHeap.pop()
        # now we need to bubble it down
        # Check if its left element exists?
        # 2i is left child, if thats within length it exists!
        while 2 * i < len(self.maxHeap):
            # Right Case
            if 2*i+1 < len(self.maxHeap) and self.maxHeap[2*i+1] < self.maxHeap[2*i] and self.maxHeap[i] > self.maxHeap[2*i+1]:
                self.maxHeap[i], self.maxHeap[2*i+1] = self.maxHeap[2*i+1], self.maxHeap[i]
                i = 2*i+1
            # Left Case
            elif self.maxHeap[i] > self.maxHeap[2*i]:
                self.maxHeap[i], self.maxHeap[2*i] = self.maxHeap[2*i], self.maxHeap[i]
                i = 2*i
            # Break Case
            else:
                break


    def add(self, val: int) -> int:
        # max heap?
        # keep track of k largest elements using a max heap?
        # Use a min heap for k elements
        # when the heap length is bigger than k we need to pop the min out
        self.push(val)
        # k'th largest should be at the top of our maxheap
        return self.maxHeap[1]


        
