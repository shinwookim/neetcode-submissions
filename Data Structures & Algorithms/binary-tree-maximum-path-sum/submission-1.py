# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_g = float("-Inf")
        def pathSum(node, currSum) -> int:
            nonlocal max_g
            
            if node is None:
                return 0
            leftSum = pathSum(node.left, 0) if node.left else 0
            rightSum = pathSum(node.right, 0) if node.right else 0

            maxPathSum = max(
                currSum + node.val,
                currSum + node.val + leftSum,
                currSum + node.val + rightSum,
            )
            max_g = max(max_g,
                node.val,
                leftSum + node.val + rightSum,
                leftSum + node.val,
                rightSum + node.val
            )
            return maxPathSum
        
        return max(pathSum(root, 0), max_g)