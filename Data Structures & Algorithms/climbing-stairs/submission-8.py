class Solution:
    def climbStairs(self, n: int) -> int:
        # bottom up..

        if n<= 2:
            return n
        one, two = 1,1
        for i in range(n-1):
            # temp equal to the current step
            temp = one
            # current step equal to current step + previous step
            one = one + two
            # tw becomes the previous set
            two = temp

        return one