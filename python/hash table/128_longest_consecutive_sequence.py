from typing import List 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        access = set(nums)
        ans = 0

        for num in access:
        
            if num - 1 not in access:
                tmp = 1 
                curr = num 

                while curr + 1 in access:
                    tmp += 1
                    curr = curr + 1

                ans = max(tmp, ans)

        return ans

