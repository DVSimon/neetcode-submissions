class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = 0
        current_max = 0
        for element in nums:
            if element == 1:
                current_max += 1
            else:
                if current_max > max_num:
                    max_num = current_max
                current_max = 0
        return max(max_num, current_max)
        