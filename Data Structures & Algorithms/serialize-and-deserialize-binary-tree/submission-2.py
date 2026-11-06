from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Traverse the tree in preorder"""
        res, stack = [], [root]
        while len(stack) > 0:
            node = stack.pop()
            if node:
                res.append(str(node.val))
                stack.append(node.right)
                stack.append(node.left)
            else:
                res.append('#')
        return ','.join(res)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        nodes = iter(data.split(','))
        def build_tree() -> Optional[TreeNode]:
            node_val = next(nodes)
            if node_val == '#':
                return None
            
            node = TreeNode(node_val)
            node.left = build_tree()
            node.right = build_tree()
            return node
        return build_tree()

