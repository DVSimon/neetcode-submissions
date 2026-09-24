class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxNum = 0
        for index in range(len(arr) - 1, -1, -1):
            num = arr[index]
            if num > maxNum:
                arr[index] = maxNum
                maxNum = num
            else:
                arr[index] = maxNum
        arr[-1] = -1
        return arr
            