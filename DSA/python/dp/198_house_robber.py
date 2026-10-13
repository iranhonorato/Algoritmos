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




    def rob_slow(self, nums: List[int]) -> int:
        """This approach works but it's slow andcauses memory consume desnecessary"""
        memo = {}

        def backtracking(idx):
            if idx >= len(nums):
                return 0
        
            if idx in memo:
                return memo[idx]

            max_from_here = 0
        
            for j in range(idx + 2, len(nums)):
                max_from_here = max(max_from_here, backtracking(j))

            memo[idx] = nums[idx] + max_from_here
            return memo[idx]

        ans = 0
        
        for i in range(len(nums)):
            ans = max(ans, backtracking(i))

        return ans





    def rob_best(self, nums: list[int]) -> int:
        """The absolutly best solution for this problem"""
        memo = {}

        def backtracking(i: int) -> int:
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]
            
            not_current = backtracking(i + 1)
            current = nums[i] + backtracking(i + 2)

            memo[i] = max(current, not_current)
            return memo[i]

        return backtracking(0)
