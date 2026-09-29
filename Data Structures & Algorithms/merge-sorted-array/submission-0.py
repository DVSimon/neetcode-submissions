class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0 # nums 1 iterator
        j = 0 # nums 2 iterator
        k = 0 # iterator for entry point to nums1

        # Do we create a temp nums1 to iterate through..?
        # I think I need to insert and shift to the right..?
        numsTemp = nums1[:] 

        while i < m and j < n:
            if numsTemp[i] <= nums2[j]:
               nums1[k] = numsTemp[i]
               i+=1
            else:
                nums1[k] = nums2[j]
                j+=1
            k+=1
        # after case for when we've gone through all of one array
        while i < m:
            nums1[k] = numsTemp[i]
            i+=1
            k+=1
        while j < n:
            nums1[k] = nums2[j]
            j+=1
            k+=1
