class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        initLength = n * 2
        ans = [0] * initLength
        for index, number in enumerate(nums):
            ans[index] = number
            ans[index + n] = number
        return ans

        