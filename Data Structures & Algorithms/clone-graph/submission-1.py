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

        clone_map = {}
        
        def dfs(n):
            # Base Case:
            if n in clone_map:
                return clone_map[n]
                
            # Loop:
            copy = Node(n.val)
            clone_map[n] = copy

            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy

        return dfs(node)



        