"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeToCopy = {None:None}
        current = head

        while current:
            copy = Node(current.val)
            nodeToCopy[current] = copy
            current = current.next
        
        current = head
        while current:
            copy = nodeToCopy[current]
            copy.next = nodeToCopy[current.next]
            copy.random = nodeToCopy[current.random]
            current = current.next
        return nodeToCopy[head]
