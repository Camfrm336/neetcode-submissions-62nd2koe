class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        visit = set()
        INF = 2147483647
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        
        dist = 0
        while q:
            qlen = len(q)
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if ((nr in range(ROWS) and nc in range(COLS)) 
                    and grid[nr][nc] == INF 
                    and (nr, nc) not in visit):
                        q.append((nr,nc))
                        visit.add((nr,nc))
            dist += 1
                    

