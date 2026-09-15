from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []

        for i in range(1,numRows + 1):
            sub = [1]*i
            ans.append(sub)
        
        if numRows == 1:
            return ans

        for i in range(numRows):
            row = i 
            for j in range(len(ans[i])):
                row_up = i - 1
                l = j - 1 
                if row_up >= 0 and l >= 0 and j < len(ans[row_up]):
                    ans[row][j] += ans[row_up][l]
                    ans[row][j] += ans[row_up][j]
                    ans[row][j] -= 1 

        return ans 