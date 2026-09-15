class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 0
        max_num = 0
        new_arr = []
        for index, element in enumerate(arr[:-1]):
            next_index = index + 1
            arr[index] = max(arr[next_index:])
        arr[-1] = -1
        return arr