class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()

        ans = list()

        ptr1 = 0 
        ptr2 = 0 

        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1] < nums2[ptr2]:
                ptr1 += 1 

            elif nums1[ptr1] > nums2[ptr2]:
                ptr2 += 1 

            else:
                ans.append(nums1[ptr1])
                ptr1 += 1
                ptr2 += 1 

        return list(set(ans))


            