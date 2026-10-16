class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return None

        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        q = deque()

        def bfs(q):
            while q:
                (row, col) = q.popleft()                         
                direction = [[1,0], [0,1], [-1,0], [0,-1]]

                for x, y in direction:
                    dr, dc = row + x, col + y
                    if (dr in range(rows) and
                        dc in range(cols) and
                        grid[dr][dc] == INF):
                        grid[dr][dc] = grid[row][col] + 1
                        q.append((dr, dc))

        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == 0):
                    q.append((r,c))
        
        bfs(q)

                            





                    
