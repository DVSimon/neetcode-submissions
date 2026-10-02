from _heapq import heapify
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # We can heapify it then pop k-1 number of times and our kth largest will get on top
        # e.g. 2,3,1,5,4 -> 1,2,3,4,5; k = 2; pop k-1 = 1 times then top is 4
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)
        for _ in range(1, k):
            heapq.heappop(maxHeap)
        return -maxHeap[0]