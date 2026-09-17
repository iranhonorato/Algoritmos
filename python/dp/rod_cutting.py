from typing import List

def cutRod(prices:int):
    memo = {}

    def backtracking(array):
        n = len(array)

        if n == 0:
            return 0 

        elif n == 1:
            return array[-1]


        if memo.get(n) is not None:
            return memo.get(n)


        memo[n] = array[-1]

        for i in range(n):
            curr = backtracking(array[:i]) + backtracking(array[:n-i])

            if curr > memo[n]:
                memo[n] = curr 

        return memo[n]
        


    return backtracking(prices)


prices = [1, 5, 8, 9, 10, 17, 17, 20]
print(cutRod(prices))
