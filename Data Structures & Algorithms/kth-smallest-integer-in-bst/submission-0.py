# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, root, result):
        """In-order traversal"""
        if root:
            self.traverse(root.left, result)
            result.append(root.val)
            self.traverse(root.right, result)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        traversed = []
        self.traverse(root, traversed)
        return traversed[k-1]