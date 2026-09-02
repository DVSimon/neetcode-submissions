from typing import List, Tuple


def sum_3_integers(triplet: List[int]) -> int:
    numberOne, numberTwo, numberThree = triplet
    return numberOne + numberTwo + numberThree


def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    length, width, height = box_dimensions
    return length * width * height
  

# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))
