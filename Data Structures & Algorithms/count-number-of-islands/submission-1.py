
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        count = 0
        seen = set()


        def bfs(r,c):
            q = deque()
            seen.add((r,c))
            q.append((r,c))
            while q:
                row,col = q.popleft()
                directions = [(1,0),(-1,0),(0,1),(0,-1)]

                for dr,dc in directions:
                    nr = dr + row
                    nc = dc + col
                    if (
                            0 <= nr < rows and
                            0 <= nc < cols and
                            grid[nr][nc] == "1" and
                            (nr, nc) not in seen
                        ):
                            seen.add((nr,nc))
                            q.append((nr,nc))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row,col) not in seen:
                    bfs(row,col)
                    count += 1
        return count

            