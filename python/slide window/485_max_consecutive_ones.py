class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        l = -1
        ans = 0 

        if len(nums) == 0:
            return ans

        for i in range(len(nums)):
            if nums[i] != 1:
                l = i

            ans = max(ans, i - l)
        return ans 

