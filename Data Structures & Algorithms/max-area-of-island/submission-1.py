
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        

        def bfs(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            count = 1

            while q:
                directions = [(1,0),(-1,0),(0,1),(0,-1)]
                row,col = q.popleft()

                for dr,dc in directions:
                    nr = dr + row
                    nc = dc + col
                    if (
                        0<= nr < rows and
                        0<= nc < cols and
                        (nr,nc) not in visited and
                        grid[nr][nc] == 1
                    ):
                        visited.add((nr,nc))
                        q.append((nr,nc))
                        count += 1
            return count
        

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == 1:
                    res = max(res,bfs(r,c))
        return res
                    