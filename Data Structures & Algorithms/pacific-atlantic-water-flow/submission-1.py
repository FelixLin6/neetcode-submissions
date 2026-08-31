from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        
        def flood(shore: List[int, int]) -> List[int, int]:
            explored = set(shore)
            Q = deque(shore)
            while Q:
                (r, c) = Q.popleft()
                for (dx, dy) in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    x, y = r + dx, c + dy
                    if x in range(n) and y in range(m) and (x, y) not in explored and heights[x][y] >= heights[r][c]: 
                        Q.append((x, y))
                        explored.add((x, y))

            return explored
        
        pacific = flood([(r, c) for r in range(n) for c in range(m) if r == 0 or c == 0 ])
        atlantic = flood([(r, c) for r in range(n) for c in range(m) if r == n-1 or c == m-1 ])

        return [[r, c] for (r, c) in pacific & atlantic]

