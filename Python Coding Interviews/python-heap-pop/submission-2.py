import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    return [heapq.heappop(heap) for i in range(len(heap))]
    # pop_list = []
    # # for element in range(len(heap)):
    # while heap:
    #     pop_list.append(heapq.heappop(heap))
    # return pop_list


# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
