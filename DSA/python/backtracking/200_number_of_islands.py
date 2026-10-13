from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0 

        def backtracking(r, c):
            if r < 0 or r >= len(grid):
                return 

            elif c < 0 or c >= len(grid[r]):
                return 

            if grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            backtracking(r+1, c) 
            backtracking(r-1, c)
            backtracking(r, c+1)
            backtracking(r, c-1)
            
            return 
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    ans += 1
                    backtracking(r, c)
        return ans