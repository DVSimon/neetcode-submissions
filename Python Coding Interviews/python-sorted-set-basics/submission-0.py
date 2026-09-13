from typing import List
from sortedcontainers import SortedSet


def get_first_three(sorted_set: SortedSet[int], nums1: List[int], nums2: List[int]) -> List[int]:
    sorted_set.update(nums1)
    for element in nums2:
        sorted_set.discard(element)
    result_list = []
    for i in range(3):
        result_list.append(sorted_set.pop(0))
    return result_list


# do not modify below this line
print(get_first_three(SortedSet(), [1, 2, 3], [4]))
print(get_first_three(SortedSet([1, 4, 7, 2, 8, 9]), [10], [1, 7, 2]))
print(get_first_three(SortedSet([1, 2, 3, 7]), [], [4, 5, 6]))
print(get_first_three(SortedSet([1, 2, 3, 4, 5, 6, 7, 8, 9]), [10, 11, 12], [1, 2, 3, 4, 5, 6, 7, 8, 9]))
