class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        res = 0

        def dfs(r, c):
            grid[r][c] = 0
            area = 1
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == 1:
                    area += dfs(nr, nc)
            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    res = max(res, area)
        return res