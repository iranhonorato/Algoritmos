from typing import List

class Solution:
    def distributeCookies(self, cookies: list[int], k: int) -> int:
        children = [0]*k
        ans = [sum(cookies)]

        def backtracking(idx):
            if idx == len(cookies):
                ans[0] = min(ans[0], max(children))
                return

            seen = set()

            for idx_child in range(k):
                if children[idx_child] in seen:
                    continue 
                seen.add(children[idx_child])
                print(seen)

                children[idx_child] += cookies[idx]

                backtracking(idx+1)

                children[idx_child] -= cookies[idx]
            return

        backtracking(0)
        return ans[0]



obj = Solution()
print(obj.distributeCookies(cookies = [6,1,3,2,2,4,1,2], k = 3))