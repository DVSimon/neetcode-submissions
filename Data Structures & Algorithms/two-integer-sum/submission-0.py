class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We can use a Brute force method I suppose o(n**2)
        #j = 0
        for index, num in enumerate(nums):
            j = index + 1
            while j < len(nums):
                if num + nums[j] == target:
                    return [index, j]
                j += 1
        return [0,0]