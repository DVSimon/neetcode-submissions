class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # I should do it with a min heap
        # since we need kth largest from nums
        # If we do a min heap with size k, then the smallest in heap is kth largest
        return heapq.nlargest(k, nums)[-1]