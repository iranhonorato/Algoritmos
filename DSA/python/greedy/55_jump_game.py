from typing import List 

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        
        for i in range(2, len(nums) + 1):
            idx = len(nums) - i
            
            if idx + nums[idx] >= goal:
                goal = idx
                
        return goal == 0



    def canJump_second_solution(self, nums: list[int]) -> bool:
        goal = len(nums) - 1 

        for i in range(len(nums)):
            pos = len(nums)-1-i
            mov = nums[pos] 
            if mov + pos >= goal:
                goal = pos 

        return goal == 0 