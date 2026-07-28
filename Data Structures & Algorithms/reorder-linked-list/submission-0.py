# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(0)
        dummy.next = head

        slow = fast = head

        # find middle split
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # sever the connection
        second_list = slow.next
        slow.next = None

        # reverse second half
        prev = None
        curr = second_list

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        second_list = prev
        first_list = head

        # Merge 2 halves
        while first_list and second_list:
            temp_first = first_list.next
            temp_second = second_list.next

            first_list.next = second_list
            second_list.next = temp_first

            first_list = temp_first
            second_list = temp_second
        
        
