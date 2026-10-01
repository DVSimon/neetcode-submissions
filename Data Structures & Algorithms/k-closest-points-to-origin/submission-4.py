class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # k = number of points to return closest to 0,0
        # points = list of points
        # d = x^2 + y^2 for our distance metric
        # sqrt here doesnt matter since its a sum...
        # So if I do quicksort, once i get a pivot with k numbers before it, we're good..
        mathFunc = lambda x: x[0] ** 2 + x[1] ** 2
        # mathFunc[l] + ....
        def partition(l,r):
            pivot = r
            pivotDist = mathFunc(points[pivot])
            idx = l
            for i in range(l, r):
                if pivotDist > mathFunc(points[i]):
                    points[idx], points[i] = points[i], points[idx]
                    idx += 1
            points[idx], points[r] = points[r], points[idx]
            return idx

        L, R = 0, len(points) - 1
        pivot = len(points)

        while pivot != k:
            pivot = partition(L, R)
            if pivot > k:
                R = pivot - 1
            else:
                L = pivot + 1
        return points[0:k]
        # pivot = len(points)
        # right = pivot-1
        # left = 0

        # # the pivot spot # can never be less than k
        # # if its equal, then we know we have k in front
        # # if its larger, we know we need another sort of the lower part of array

        # while pivot != k:
        #     print("Test")
        #     pivotDist = ((points[right][0])**2) + ((points[right][1])**2)
        #     for i in range(0, right):
        #         iterDist = ((points[i][0])**2) + ((points[i][1])**2)
        #         if iterDist < pivotDist:
        #             temp = points[left]
        #             points[left] = points[i]
        #             points[i] = temp
        #             left += 1
        #     # We need to swap pivot point and left
        #     temp = points[left]
        #     points[left] = points[right]
        #     points[right] = temp
        #     pivot = left
        #     if pivot < k:
        #         left = pivot + 1
        #     else:
        #         right = pivot - 1
        # return points[0:k]
        