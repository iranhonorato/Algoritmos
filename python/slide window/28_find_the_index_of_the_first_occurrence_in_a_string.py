class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = 0 
        r = len(needle)

        while r <= len(haystack):
            if haystack[l:r] == needle:
                return l 
            
            r +=1
            l += 1 

        return -1