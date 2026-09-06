from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Principal: 1 -> 2 -> 3 -> 4 -> 5 -> None
# Reverse: 5 -> 

class Solution:
    def reverseList_recursion(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def backtracking(curr):
            if curr.next is None or curr is None:
                return curr

            node = backtracking(curr.next)
            node.next = curr
            node.next.next = None
            return node

        return backtracking(head)


    def reverseList_loop(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass 
