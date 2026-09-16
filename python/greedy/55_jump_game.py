from typing import List 

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        
        for i in range(2, len(nums) + 1):
            idx = len(nums) - i
            
            if idx + nums[idx] >= goal:
                goal = idx
                
        return goal == 0