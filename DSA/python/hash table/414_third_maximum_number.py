class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        filter = list(set(nums))
        filter.sort()
        
        if len(filter) < 3:
            return filter[-1]

        return filter[len(filter)-3]
