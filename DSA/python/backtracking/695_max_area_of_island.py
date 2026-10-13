class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        answer = 0

        def dfs(r, c):
            
            if r < 0 or r >= len(grid):
                return 0
            
            elif c < 0 or c >= len(grid[r]):
                return 0

            elif grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0 
            area = 1 
            
            area += dfs(r-1, c)
            area += dfs(r+1, c)
            area += dfs(r, c-1)
            area += dfs(r, c+1)

            return area
    
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    area = dfs(r,c)
                    answer = max(answer, area)
        return answer