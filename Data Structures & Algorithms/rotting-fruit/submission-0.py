from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:        
        n, m = len(grid), len(grid[0])        
        def bfs(i, j):
            queue = deque([(i, j, 0)])
            while queue:
                i, j, dist = queue.popleft()

                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if 0 <= i + di < n and 0 <= j + dj < m:
                        if grid[i + di][j + dj] == 1 or grid[i + di][j + dj] < dist - 1:
                            grid[i + di][j + dj] = dist - 1
                            queue.append((i + di, j + dj, dist - 1))


        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    bfs(i, j)
        time_needed = 0
    
        for i in range(n):
            for j in range(m):
                time_needed = min(time_needed, grid[i][j])
                if grid[i][j] == 1:
                    return -1
        return -1 * time_needed

