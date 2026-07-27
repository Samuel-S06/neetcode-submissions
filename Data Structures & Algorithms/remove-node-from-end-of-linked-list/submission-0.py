# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # make dummy var but also make left = first node
        # then make a right node, n spaces right of left
        # slide this window until right = None
        # then remove the left node, and then return dummy.next

        dummy = ListNode(0)
        dummy.next = head
        
        left = dummy
        right = head

        for i in range(n):
            right = right.next

        while right:
            right = right.next
            left = left.next
        
        left.next = left.next.next

        return dummy.next

        
        

        
        
        