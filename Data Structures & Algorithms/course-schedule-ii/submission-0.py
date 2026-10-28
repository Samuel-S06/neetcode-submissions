class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict

        indeg = [0] * numCourses
        adjList = defaultdict(list)
        q = deque()
        path = []

        # find indegree of nodes & build adjList
        for a, b in prerequisites:
            indeg[a] += 1
            adjList[b].append(a)
        
        # put indegree of 0 to queue
        for i in range(len(indeg)):
            if indeg[i] == 0:
                q.append(i)
        
        def bfs(q):
            while q:
                num = q.popleft()
                path.append(num) 

                for nei in adjList[num]:
                    indeg[nei] -= 1
                    if indeg[nei] == 0:
                        q.append(nei)   
        bfs(q)

        # if valid ordering exists from topo sort: return path
        if len(path) != numCourses:
            return []
        else: 
            return path

        