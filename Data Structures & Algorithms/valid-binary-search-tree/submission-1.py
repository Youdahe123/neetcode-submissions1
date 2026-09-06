# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def valid(root,min1,max1):
            if not root:
                return True
            if not (min1<root.val<max1):
                return False
            left = valid(root.left,min1,root.val)
            right = valid(root.right,root.val,max1)
            return left and right
        return valid(root,float('-inf'),float('inf'))

        