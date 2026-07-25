# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #[7, 0, 8]
        #carry (6 + 4 = 10) = 1 sum // 10 = 1
        #14 carry 1
        dummy = head = ListNode()
        carry = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = (v1 + v2 + carry) % 10
            carry = (v1 + v2 + carry) // 10
            head.next = ListNode(val)
            head = head.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            head.next = ListNode(1)
            
        return dummy.next