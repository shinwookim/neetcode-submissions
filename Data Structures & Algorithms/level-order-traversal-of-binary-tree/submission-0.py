# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result, Q, level = [], deque(), 0
        Q.append((level, root))

        while len(Q) > 0:
            (level, node) = Q.popleft()

            if level >= len(result):
                result.append([node.val])
            else:
                result[level].append(node.val)
            
            if node.left:
                Q.append((level + 1, node.left))
            if node.right:
                Q.append((level + 1, node.right))

        return result