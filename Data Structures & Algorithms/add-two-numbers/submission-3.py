# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # iterate through each
        # num1 = 0
        # num2 = 0
        # i = 1
        # while l1:
        # num1 += li.val * i
        # i *= 10
        # do same for l2
        # add num1 and num2

        dummy = curr = ListNode(0)
        carry = 0
        digit = 0

        while l1 and l2:
            total = l1.val + l2.val + carry
            digit = total % 10
            carry = total // 10

            curr.next = ListNode(digit)

            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        if not l1:
            while l2:
                total = l2.val + carry
                digit = total % 10
                carry = total // 10

                curr.next = ListNode(digit)
                
                curr = curr.next
                l2 = l2.next
        else:
            while l1:
                total = l1.val + carry
                digit = total % 10
                carry = total // 10

                curr.next = ListNode(digit)

                curr = curr.next
                l1 = l1.next

        if carry:
            curr.next = ListNode(carry)

        return dummy.next

        

        