"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        copied = {node: Node(node.val)}
        stack = [node]

        while stack:
            curr = stack.pop()

            for neighbor in curr.neighbors:
                if neighbor not in copied:
                    copied[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                copied[curr].neighbors.append(copied[neighbor])

        return copied[node]