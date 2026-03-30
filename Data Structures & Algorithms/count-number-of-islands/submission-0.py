class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        islands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    q.append((r,c))
                    while q:
                        r, c = q.popleft()
                        grid[r][c] = "0"
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if ((nr in range(ROWS) and nc in range(COLS)) and grid[nr][nc] == "1"):
                                q.append((nr,nc))
                    islands += 1                    
        return islands