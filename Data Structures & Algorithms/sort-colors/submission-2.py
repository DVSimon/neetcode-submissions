class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # We know values can only be in 0 - 1 - 2 range
        # Specified range to sort = Bucket Sort

        counts = [0] * 3

        for n in nums:
            counts[n] += 1

        index = 0
        for x in range(len(counts)):
            for j in range(counts[x]):
                nums[index] = x
                index += 1


        