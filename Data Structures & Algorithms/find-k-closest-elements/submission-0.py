class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k

        while l<r:
            m = (l+r)//2
            # we arent comparing arr[m] to the target, we are comparing 
            # where the target is closer to a point.
            # 
            # if the distance of (x-arr[m]) is greater than the distance of (arr[m+k] -x)
            # we need to shift the window right; otherwise left or stay


            # BASICALLY CHECKING TO SEE IF THE DISTANCE AT MID POINT IS LARGER THAN DISTANCE AT MIDDLE+K(we take K points!) points; if this distance is larger than m+k point is closer to target so we should search on that side!
            if x - arr[m] > arr[m+k] - x:
                l = m+1
            else:
                r=m
            # we keep doing this

        return arr[l:l+k]


