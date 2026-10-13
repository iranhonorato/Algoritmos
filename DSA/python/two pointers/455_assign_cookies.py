from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        idx_g = 0
        idx_s = 0

        ans = 0 

        while idx_g < len(g) and idx_s < len(s):
            if g[idx_g] <= s[idx_s]:
                ans += 1 
                idx_g += 1 
                idx_s += 1

            else:
                idx_s += 1
                

        return ans


