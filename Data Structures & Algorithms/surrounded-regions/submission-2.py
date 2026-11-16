class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c):
            visited.add((r,c))

            directions = [[1,0], [0,1], [-1,0], [0,-1]]
            for x, y in directions:
                dr, dc = r + x, c + y

                if (dr in range(rows) and
                    dc in range(cols) and
                    (dr, dc) not in visited and
                    board[dr][dc] == "O"):
                    dfs(dr, dc)

        for row in range(rows):
            if board[row][0] == 'O':
                dfs(row, 0)
            if board[row][cols-1] == 'O':
                dfs(row, cols - 1)

        for col in range(cols):
            if board[0][col] == 'O':
                dfs(0, col)
            if board[rows-1][col] == 'O':
                dfs(rows - 1, col)

        for r in range(rows):
            for c in range(cols):
                if ((r, c) not in visited and
                    board[r][c] == 'O'):
                    board[r][c] = 'X'
        return 

        