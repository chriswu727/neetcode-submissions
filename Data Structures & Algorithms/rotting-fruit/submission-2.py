class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid),len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        fresh = 0
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])
                elif grid[r][c] == 1:
                    fresh += 1
        time = 0

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == 1:
                        q.append([nr, nc])
                        fresh -= 1
                        grid[nr][nc] = 2
            time += 1
            

        return time if fresh == 0 else -1