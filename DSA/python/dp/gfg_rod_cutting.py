class Solution:
    def cutRod_tle(self, prices: list[int]) -> int:
        memo = {}

        def backtracking(array):
            n = len(array)

            if n == 0:
                return 0

            elif n == 1:
                return array[0]

            if memo.get(n) is not None:
                return memo.get(n)

            memo[n] = array[-1]

            for k in range(n):
                profit = backtracking(array[:k]) + backtracking(array[:n-k])

                if memo[n] < profit:
                    memo[n] = profit 

            return memo[n]


        return backtracking(prices[:])

    def cutRod_best(self, prices:list[int]) -> int:
        n = len(prices)
        memo = dict()

        def backtracking(n):
            if n == 0:
                return 0 

            elif n == 1:
                return prices[0]


            elif memo.get(n) is not None:
                return memo.get(n)

            max_profit = 0 

            for k in range(n):
                profit = prices[k] + backtracking(n-1-k)

                if profit > max_profit:
                    max_profit = profit

            memo[n] = max_profit
            return memo[n]

        return backtracking(n)




