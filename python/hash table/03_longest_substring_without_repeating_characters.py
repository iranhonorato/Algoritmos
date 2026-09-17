class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memo_pos = {}

        l = 0
        ans = 0
        for i in range(len(s)):
            if memo_pos.get(s[i]) is None:
                memo_pos[s[i]] = i

            else:
                if l < memo_pos[s[i]] + 1:
                    l = memo_pos[s[i]] + 1
                memo_pos[s[i]] = i 


            ans = max(ans, i-l+1)

        return ans 


obj = Solution()
print(obj.lengthOfLongestSubstring("ccbbcc"))