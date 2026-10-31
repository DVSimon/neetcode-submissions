class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_len = len(nums)*2
        ans = [0] * new_len
        for i in range(len(nums)):
            ans[i] = ans[i + len(nums)] = nums[i]
        return ans