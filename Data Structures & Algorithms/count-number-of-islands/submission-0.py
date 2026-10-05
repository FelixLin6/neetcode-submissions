from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def bfs(i0, j0):
            Q = deque([(i0, j0)])

            while Q:
                (i, j) = Q.popleft()
                for (i2, j2) in [(i + dx, j + dy) for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]]:
                    if i2 in range(m) and j2  in range(n) and grid[i2][j2] == "1" and (i2, j2) not in explored:
                        explored.add((i2, j2))
                        Q.append((i2, j2))

        islands = 0
        explored = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in explored:
                    explored.add((i, j))
                    bfs(i, j)
                    islands += 1
                    

        return islands