class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        area = 0

        def dfs(r, c):
            direction = [[1,0], [0,1], [-1,0], [0,-1]]

            if (r not in range(rows) or
                c not in range(cols) or
                grid[r][c] == 0 or 
                (r, c) in visited):
                return 0

            visited.add((r,c))
            cell_area = 1

            for (x, y) in direction:
                dr = r + x
                dc = c + y
                cell_area += dfs(dr, dc)
            
            return cell_area
         


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = max(area, dfs(r, c))

        return area