from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = list()
        tmp = list()
        
        def backtracking():
            if len(tmp) == len(nums):
                ans.append(tmp[:])
                return 

            for i in range(len(nums)):
                if nums[i] not in tmp:
                    tmp.append(nums[i])
                    backtracking()
                    tmp.pop()
            return
            

        backtracking()
        return ans 

