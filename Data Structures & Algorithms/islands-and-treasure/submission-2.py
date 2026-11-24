from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        def bfs(x, y):
            queue = deque([(x, y, 0)])
            while queue:
                i, j, dist = queue.popleft()
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[0]) and grid[i + di][j + dj] > dist + 1:
                        grid[i + di][j + dj] =  dist + 1
                        queue.append((i + di, j + dj, dist + 1))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    bfs(i, j)