class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s_list = [char for char in s]
        goal_list = [char for char in goal]

        def rotate(array, l, r):
            if l < 0 or r >= len(array):
                return
            while l <= r:
                array[l], array[r] = array[r], array[l]
                l += 1 
                r -= 1 
            return

        count = 0 

        while count <= len(s):
            rotate(s_list, 0, len(s_list)-1)
            rotate(s_list, 0, 0)
            rotate(s_list, 1, len(s_list)-1)

            if s_list == goal_list:
                return True
            
            count += 1
        
        return False


    def rotateString2(self, s: str, goal: str) -> bool:
        s_list = [char for char in s]
        goal_list = [char for char in goal]

        count = 0 

        while count <= len(s):
            s_list = s_list[-1:] + s_list[:-1]

            if s_list == goal_list:
                return True
            
            count += 1
        
        return False




s = "dawhwh"
goal = "hdawhw"

obj = Solution()
print(obj.rotateString(s, goal))