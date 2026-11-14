class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)

        # nums[:] altera o original quando recebe uma atribuição
        nums[:] = nums[-k:-1] + nums[:-k]


        return 