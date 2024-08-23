from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            q.append([r, c])
            visit.add((r, c))
            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    new_r = dr + row
                    new_c = dc + col
                    if(
                        new_r in range(rows) and
                        new_c in range(cols) and
                        (new_r, new_c) not in visit and
                        grid[new_r][new_c] == "1"
                    ):
                        q.append([new_r, new_c])
                        visit.add((new_r, new_c))

        island = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    island += 1
        return island