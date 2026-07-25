# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle and split
        # reverse second half
        # zip back and forth

        current = head
        fast = current
        slow = current 

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        secondHalf = slow.next
        slow.next = None

        prev = None 

        while secondHalf:
            next_node = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf
            secondHalf = next_node
        
        first = head
        second = prev

        while second:
            firstNext = first.next
            secondNext = second.next
            first.next = second
            second.next = firstNext
            first = firstNext
            second = secondNext
        

        