class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        cur_big = -1
        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = cur_big
            cur_big = max(cur_big, temp)
        return arr