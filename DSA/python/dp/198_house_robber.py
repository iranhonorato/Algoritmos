from typing import List

class Solution:
    def rob_tle(self, nums: List[int]) -> int:
        """It's a good aproach but causes TLE in case 67/70"""
        ans = 0
        tmp = [0]
        memo = {}

        def backtracking(idx, curr):
            if idx in memo and curr <= memo[idx]:
                return
            
            memo[idx] = curr

            if curr > tmp[0]:
                tmp[0] = curr

            for j in range(idx + 2, len(nums)):
                new = curr + nums[j]
                backtracking(j, new)

            return

        for i in range(len(nums)):
            backtracking(i, nums[i])
            ans = max(tmp[0], ans)

        return ans 


    def rob(self, nums):
        memo = {}

        def backtracking(house):
            if house >= len(nums):
                return 0 

            elif house in memo:
                return memo[house]

            for idx in range(house, len(nums)):
                curr = nums[idx] + backtracking(idx + 2)
                next = backtracking(idx+1)

                memo[idx] = max(curr, next)

            return memo[house]





    def rob_best(self, nums: list[int]) -> int:
        """The absolutly best solution for this problem"""
        memo = {}

        def backtracking(house: int) -> int:
            if house >= len(nums):
                return 0

            if house in memo:
                return memo[house]
            
            not_current = backtracking(house + 1)
            current = nums[house] + backtracking(house + 2)

            memo[house] = max(current, not_current)
            return memo[house]

        return backtracking(0)
