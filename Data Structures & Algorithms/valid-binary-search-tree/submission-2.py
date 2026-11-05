# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recursiveValidation(self, root: TreeNode, interval: List[int]) -> bool:
        if root is None:
            return True
        if root.val <= interval[0] or root.val >= interval[1]:
            return False   
        return self.recursiveValidation(root.left, [interval[0], root.val]) \
            and self.recursiveValidation(root.right, [root.val, interval[1]])
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.recursiveValidation(root,[-1000000000 ,1000000000])