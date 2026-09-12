from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        space = ["."]*n
        
        board = []
        for i in range(n):
            board.append(space[:])

        ans = []

        # memory where we can't put a queen
        nc  = [] # column
        pd  = [] # principal diagonal
        sd  = [] # secundary diagonal 

        def fill(r, nc, pd, sd):
            if r >= len(board):
                copy = board[:]
                for i in range(len(copy)):
                    copy[i] = "".join(copy[i])
                ans.append(copy)
                return 

            for c in range(len(board[r])):
                curr_pd = r + c 
                curr_sd = r - c

                if c not in nc and curr_pd not in pd and curr_sd not in sd: 
                    board[r][c] = "Q"

                    nc.append(c)
                    pd.append(curr_pd)
                    sd.append(curr_sd)

                    fill(r+1, nc, pd, sd)

                    board[r][c] = "."
                    nc.pop()
                    pd.pop()
                    sd.pop()
            
            return
        
        fill(0, nc, pd, sd)
        return ans