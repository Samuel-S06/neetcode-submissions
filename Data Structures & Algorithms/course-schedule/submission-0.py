class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict

        if not prerequisites and numCourses > 0:
            return True
        
        if numCourses == 0:
            return False

        adjList = defaultdict(list)
        inDeg = [0] * numCourses
        completed = 0
        q = deque()

        for u, v in prerequisites:
            inDeg[u] += 1
            adjList[v].append(u)
        
        for i in range(len(inDeg)):
            if inDeg[i] == 0:
                q.append(i)
        
        def bfs(q):
            nonlocal completed
            while q:
                u = q.popleft()
                completed += 1

                for nei in adjList[u]:
                    inDeg[nei] -= 1

                    if inDeg[nei] == 0:
                        q.append(nei)

        bfs(q)

        if completed < numCourses:
            return False
        else:
            return True

        