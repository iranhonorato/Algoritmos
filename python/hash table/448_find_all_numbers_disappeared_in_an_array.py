class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        length = len(nums)
        count = 1 
        map = set(nums)
        ans = list()
        while count <= length:
            if count not in map:
                ans.append(count)
            count += 1 

        return ans

    
    