class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        cnt = 0

        def dfs(r, c):
            grid[r][c] = "0"
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == "1":
                    dfs(nr, nc)
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    cnt += 1
        return cnt