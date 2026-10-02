class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Either keep a max heap and pop out two elements
        # OR keep a min heap and constantly check it against others..?

        # Lets do max heap
        maxHeap = [-num for num in stones]
        heapq.heapify(maxHeap)
        # We need to smash the elements together each time
        # o(n)
        while len(maxHeap) > 1:
            # heap pop is o(1)
            firstHighest = heapq.heappop(maxHeap)
            secondHighest = heapq.heappop(maxHeap)
            if firstHighest == secondHighest:
                continue
            else:
                newWeight = abs((-firstHighest) - (-secondHighest))
                heapq.heappush(maxHeap, -newWeight)
        if maxHeap:
            return -maxHeap[0]
        return 0