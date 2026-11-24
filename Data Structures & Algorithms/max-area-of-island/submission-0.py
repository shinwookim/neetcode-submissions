class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            grid[i][j] = 0
            area = 1 
            if 0 < i and grid[i - 1][j] == 1:
                area += dfs(i - 1, j)
            if i < len(grid) -1 and grid[i + 1][j] == 1:
                area += dfs(i + 1, j)
            if 0 < j and grid[i][j - 1] == 1:
                area += dfs(i, j - 1)
            if j < len(grid[0]) -1 and grid[i][j + 1] == 1:
                area += dfs(i, j + 1)
            
            return area

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        return max_area