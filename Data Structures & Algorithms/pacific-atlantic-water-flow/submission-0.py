class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        n, m = len(heights), len(heights[0])

        def flood(starts):
            seen = set(starts)
            stack = list(starts)
            while stack:
                r, c = stack.pop()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    x, y = r + dr, c + dc
                    if (0 <= x < n and 0 <= y < m
                            and (x, y) not in seen
                            and heights[x][y] >= heights[r][c]):
                        seen.add((x, y))
                        stack.append((x, y))
            return seen

        pacific = flood([(0, c) for c in range(m)] + [(r, 0) for r in range(n)])
        atlantic = flood([(n - 1, c) for c in range(m)] + [(r, m - 1) for r in range(n)])
        return [[r, c] for r, c in pacific & atlantic]