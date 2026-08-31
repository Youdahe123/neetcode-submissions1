# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not q and p:
            return False
        if q and not p:
            return False


        qRes = []
        pRes = []
        first = deque([q])
        second = deque([p])

        while first:
            levelSize = len(first)
            levelNodes = []
            for i in range(levelSize):
                node = first.popleft()
                levelNodes.append(node.val)
                if node.left:
                    first.append(node.left)
                if node.right:
                    first.append(node.right)
                else:
                    levelNodes.append("None")
            qRes.append(levelNodes)
        while second:
            levelSize = len(second)
            levelNodes = []
            for i in range(levelSize):
                node = second.popleft()
                levelNodes.append(node.val)
                if node.left:
                    second.append(node.left)
                if node.right:
                    second.append(node.right)
                else:
                    levelNodes.append("None")
            pRes.append(levelNodes)
        return qRes == pRes
                
        