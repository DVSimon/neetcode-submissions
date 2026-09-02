from typing import List


def disallow_negatives(num: int) -> int:
    number = max(0, num)
    return number


def max_difference(nums: List[int]) -> int:
    highDiff, prev_number = 0, 0
    for i, n in enumerate(nums):
        if i == 0:
            prev_number = n
            continue
        if n-prev_number > highDiff:
            highDiff = n-prev_number   
        prev_number = n
    return highDiff 




# do not modify below this line
print(disallow_negatives(-2))
print(disallow_negatives(-1))
print(disallow_negatives(0))
print(disallow_negatives(1))
print(disallow_negatives(2))

print(max_difference([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(max_difference([1, 2, 3, 4, 5, 6, 8, 9]))
print(max_difference([10, 1, 3, 7]))
print(max_difference([2, 4, 7, 5, 7, 8, 4, 2]))
