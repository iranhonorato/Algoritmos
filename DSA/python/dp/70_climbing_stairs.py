class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}
        
        def recursion(n):

            if n in memo:
                return memo[n]

            elif n <= 1:
                memo[n] = 1
                return memo[n]

            soma = recursion(n-1) + recursion(n-2)
            memo[n] = soma
            return soma


        return recursion(n)
            