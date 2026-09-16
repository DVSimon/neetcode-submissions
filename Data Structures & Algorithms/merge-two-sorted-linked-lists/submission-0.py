# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = node = ListNode() #creating a dummy node at the start
        while list1 and list2: # if both lists have elements compare the head(lowest)
            if list1.val < list2.val: 
                node.next = list1 # set the new list next node as list1 head
                list1 = list1.next #list1 head moves to next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next # move the node list over so we dont replace the same element

        node.next = list1 or list2 # if any left in either we set the rest of that in new list

        return head.next # returning the next of the dummy which is the start of node
            
