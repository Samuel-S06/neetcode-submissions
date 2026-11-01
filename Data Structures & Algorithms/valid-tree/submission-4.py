class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import defaultdict

        if n == 0:
            return False

        if len(edges) == 0:
            return True

        adjList = defaultdict(list)
        visited = set()

        # make adj list
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)
        
        # dfs to find cycles
        def dfs(node, parent):
            visited.add(node)
            
            for nei in adjList[node]:
                # if there is a potential cycle
                if nei in visited:
                    if nei == parent :
                        continue
                    else:
                        return False

                if not dfs(nei, node):
                    return False
                
            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n