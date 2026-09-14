class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num, current_max = 0, 0
        # for element in nums:
        #     if element == 1:
        #         current_max += 1
        #     else:
        #         if current_max > max_num:
        #             max_num = current_max
        #         current_max = 0
        # return max(max_num, current_max)
        for num in nums:
            current_max = current_max + 1 if num else 0
            max_num = max(max_num, current_max)
        return max_num