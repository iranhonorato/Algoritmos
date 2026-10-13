from typing import List 


class Solution:
    def isValid(self, s: str) -> bool:
        register = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        

        stack = []

        for letter in s:
            if letter in "([{":
                stack.append(register[letter])

            else:
                if len(stack) == 0:
                    return False

                top = stack.pop()

                if letter != top:
                    return False
        
        return len(stack) == 0
