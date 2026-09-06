from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}

        for i in range(len(nums)):
            if memo.get(nums[i]) is not None:
                return [memo[nums[i]], i]
            
            else:
                memo[target-nums[i]] = i 

        return [-1, -1]