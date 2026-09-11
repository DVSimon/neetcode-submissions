import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    newList = []
    for num in nums:
        pair = (-num, num)
        heapq.heappush(newList, pair)
    maxList = []
    while newList:
        pair = heapq.heappop(newList)
        original_num = pair[1]
        maxList.append(original_num)
    return maxList



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
