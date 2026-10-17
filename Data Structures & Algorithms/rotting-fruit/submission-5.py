class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        rows, cols = len(grid), len(grid[0])
        fresh_fruit = 0
        minutes = 0
        q = deque()

        def bfs(q):
            nonlocal minutes, fresh_fruit
            while q: 
                for _ in range(len(q)):
                    (row, col) = q.popleft()

                    direction = [[1,0], [0,1], [-1,0], [0,-1]]

                    for x, y in direction:
                        dr, dc = row + x, col + y

                        if (dr in range(rows) and dc in range(cols) and
                            grid[dr][dc] == 1):
                            grid[dr][dc] = 2
                            fresh_fruit -= 1
                            q.append((dr, dc))

                minutes += 1


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh_fruit += 1

        if fresh_fruit == 0:
            return 0

        bfs(q)

        if fresh_fruit > 0:
            return -1
        else:
            return minutes - 1
