class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        q = deque()

        # also serve as visited set for both sides
        pac_reachable = set()
        atl_reachable = set()

        def bfs(q, reachable_set):
            while q:
                row, col = q.popleft()

                directions = [[0,1], [1,0], [0,-1], [-1,0]]
                for x, y in directions:

                    dr, dc = row + x, col + y
                    if (dr in range(rows) and
                    dc in range(cols) and
                    (dr, dc) not in reachable_set and
                    heights[row][col] <= heights[dr][dc]):
                        reachable_set.add((dr, dc))
                        q.append((dr, dc))
                    
        # Pacific cells
        for row in range(rows):
            pac_reachable.add((row, 0))
            q.append((row, 0))
        for col in range(cols):
            pac_reachable.add((0, col))
            q.append((0, col))
        
        bfs(q, pac_reachable)
        
        # Atlantic cells

        for row in range(rows):
            atl_reachable.add((row, cols - 1))
            q.append((row, cols - 1))
        for col in range(cols):
            atl_reachable.add((rows - 1, col))
            q.append((rows - 1, col))
        
        bfs(q, atl_reachable)

        # result
        result = []
        for row in range(rows):
            for col in range(cols):
                if ((row, col) in pac_reachable and
                    (row, col) in atl_reachable):
                    result.append((row, col))
        
        return result
        
        