class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict
        visited = set()
        cc_count = 0

        #build adjacency list
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        # dfs
        def dfs(node):
            for nei in adjList[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                cc_count += 1

        return cc_count
        