# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:



        def dfs(node,maxVal):
            if not node:
                return 0
            
            res = 2 if node.val >= maxVal else 1
            maxVal = max(maxVal,node.val)
            res += dfs(node.left,maxVal)
            res += dfs(node.right,maxVal)
            return res - 1
        return dfs(root,root.val)
        