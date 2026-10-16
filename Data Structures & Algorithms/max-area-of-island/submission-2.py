class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def dfs(row, col):
            if not (row in range(rows) and col in range(cols) and 
                (row, col) not in visited  and grid[row][col] == 1):
                return 0
           
            visited.add((row, col))
            area = 1
            direction = [[1,0], [0,1], [-1,0], [0,-1]]
            
            for x, y in direction:
                dr, dc = row + x, col + y
                area += dfs(dr, dc)
            
            return area

        for r in range(rows):
            for c in range(cols):
                if ((r,c) not in visited and
                    grid[r][c] == 1):
                    max_area = max(max_area, dfs(r,c))

        return max_area 


        