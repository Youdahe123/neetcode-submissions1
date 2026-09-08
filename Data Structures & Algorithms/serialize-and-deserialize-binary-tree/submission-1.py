# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        q = deque([root])

        res = []
        strRes = ""

        while q:
            levelSize = len(q)
            levelNodes = []
            if all(n is None for n in q):
                break
            for i in range(levelSize):
                node = q.popleft()
                if node is None:
                    levelNodes.append('None')
                    continue
                levelNodes.append(node.val)
                q.append(node.left)      # push whatever it is — node or None
                q.append(node.right)
            res.append(levelNodes)
        flatten = [i for row in res for i in row]
        for x in flatten:
            strRes += ('N' if x == 'None' else str(x)) + ','
        return strRes


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        splitted = data.split(',')
        splitted = [None if i == 'N' else int(i) for i in splitted if i != '']
        root = TreeNode(splitted[0])
        q = deque([root])
        i = 1
        while q and i + 1 < len(splitted):
            parent = q.popleft()

            if i < len(splitted) and splitted[i] is not None:
                parent.left = TreeNode(splitted[i])
                q.append(parent.left)
            if i < len(splitted) and splitted[i + 1] is not None:
                parent.right = TreeNode(splitted[i + 1])
                q.append(parent.right)
            i += 2
        return root

            
