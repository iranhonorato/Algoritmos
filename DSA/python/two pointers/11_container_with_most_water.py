from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int: 
        ans = 0 

        l = 0 
        r = len(height) - 1 
        while l <= r:
            left = height[l]
            right = height[r]

            x = r - l

            if left > right:
                y = right
                r -= 1
            
            else:
                y = left
                l += 1 

            if x*y > ans:
                ans = x*y 


        return ans


obj = Solution()
print(obj.maxArea([1,8,6,2,5,4,8,3,7]))