from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = list()
        tmp = list()

        def backtracking(idx):
            if idx >= len(nums):
                ans.append(tmp[:])
                return

            tmp.append(nums[idx])
            backtracking(idx+1)
            
            tmp.pop()
            backtracking(idx+1)

            return
        
        backtracking(0)
        return ans 