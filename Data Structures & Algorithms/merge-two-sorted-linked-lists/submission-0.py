# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = curr = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next
        
        if not list1:
            curr.next = list2
        else:
            curr.next = list1

        return dummy.next
        # head = curr = min of both heads
        # so we have a head for each
        # meanwhile a list is non empty
        # if list1 head <= list2 head --> curr.next = list1 head and list1.next
        # else: list2 head and list2.next
        # if list 1 is empty --> append list 2
        # else: appendlist 2

        # return head

        