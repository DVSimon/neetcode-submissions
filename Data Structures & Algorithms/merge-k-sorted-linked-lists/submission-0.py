# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # What if I continously merge the last two linked lists..?
        # e.g. Merge from mergesort the last two arrays n and n-1
        # at each step replace n-1 with merged
        #eventually on big array..?
        if len(lists) == 0:
            return None

        n = len(lists) - 1
        while n > 0:
            # LL Comparisons
            newNode = ListNode()
            tail = newNode

            l1 = lists[n-1]
            l2 = lists[n]

            while l1 and l2:
                if l1.val <= l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            if l1:
                tail.next = l1
            if l2:
                tail.next = l2
            # now we have a merged LL in newNode.next
            lists[n-1] = newNode.next
            lists.pop()
            n -= 1
        return lists[0]




        #     # Code for comparisons
        #     arr1 = lists[n-1]
        #     arr2 = lists[n]
        #     i, j, z = 0, 0, 0
        #     f, k = len(arr1), len(arr2)
        #     resArr = [0] * (f + k)
        #     while i < f and j < k:
        #         if arr1[i] <= arr2[j]:
        #             resArr[z] = arr[i]
        #             i+=1
        #         else:
        #             resArr[z] = arr[j]
        #             j+=1
        #         z+=1
        #     # Finish merging after one is done
        #     while i < f:
        #         resArr[z] = arr[i]
        #         i+=1
        #         z+=1
        #     while j < k:
        #         resArr[z] = arr[j]
        #         j+=1
        #         z+=1
        #     # Set second to last equal to merged sort array
        #     lists[n-1] = res[Arr]
        #     # Remove last element
        #     lists.pop()
        #     # Decrement n til n-1 is first array
        #     n-=1
        # return lists

        