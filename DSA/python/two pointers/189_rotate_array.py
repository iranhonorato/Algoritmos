class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)

        # nums[:] altera o original quando recebe uma atribuição
        nums[:] = nums[-k:] + nums[:-k]


        return 


    def rotate2(self, nums:list[int], k:int) -> None:

        k = k % len(nums)

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
            return

        reverse(0, len(nums)-1)
        reverse(0, k-1)
        reverse(k, len(nums)-1)
        return  
