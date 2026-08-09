# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        groupPrev = dummy 


        while True:
            kth = self.getKth(groupPrev,k)
            if not kth:
                break
            groupNext = kth.next

            # reverse groupNext
            prev = kth.next
            current = groupPrev.next

            while current != groupNext:
                nextNode = current.next
                current.next = prev
                prev = current
                current = nextNode
            nextNode = groupPrev.next
            groupPrev.next = kth
            groupPrev = nextNode
        return dummy.next

    
    def getKth (self,curr , k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
        