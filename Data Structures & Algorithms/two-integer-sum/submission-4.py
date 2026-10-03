class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary attempt
        # Use a dictionary and at each value subtract the num from target
        # if said value is in dictionary, we have our match
        # if not, add the value:index pair
        dictCheck = {}
        for index, num in enumerate(nums):
            checkSub = target - num
            if checkSub in dictCheck:
                return [dictCheck[checkSub], index]
            else:
                dictCheck[num] = index

        return [0,0]