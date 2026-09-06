# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot:
            return True
        if not root:
            return False
        if root.val == subRoot.val:
            if self.isSameTree(subRoot,root):
                return True
        
        left = self.isSubtree(root.left,subRoot)
        right = self.isSubtree(root.right,subRoot)
        if left or right:
            return True
        return False

    def isSameTree(self,sub,real):
        if not sub and not real:
            return True
        if not real and sub:
            return False
        if not sub and real:
            return False
        if sub.val != real.val:
            return False
        left = self.isSameTree(sub.left,real.left)
        right = self.isSameTree(sub.right,real.right)
        if left and right:
            return True
        else:
            return False

        
        