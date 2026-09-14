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
        o2n = {}

        def dfs(node):
            if node in o2n:
                return o2n[node]
            cpy = Node(node.val)
            o2n[node] = cpy
            for nei in node.neighbors:
                cpy.neighbors.append(dfs(nei))
            return cpy
        return dfs(node)

