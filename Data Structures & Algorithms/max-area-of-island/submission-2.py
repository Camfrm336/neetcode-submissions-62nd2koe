class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        maxArea = 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        for r in range(ROWS):
            for c in range(COLS):
                area = 0
                if grid[r][c] == 1:
                    q.append((r,c))
                    grid[r][c] = 0
                    area += 1
                    while q:
                        qlen = len(q)
                        r, c = q.popleft()
                        grid[r][c] = 0
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if (nr in range(ROWS) and nc in range(COLS)) and grid[nr][nc] == 1:
                                q.append((nr,nc))
                                area += 1
                                print(area)
                    maxArea = max(area, maxArea)
        return maxArea

        