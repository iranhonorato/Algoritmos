# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:

        if head is None or head.next is None or k == 0:
            return head

        def length_list(head):
            l = 0 
            while head is not None:
                head = head.next
                l += 1 
            return l 

        k = k % length_list(head)
        
        def rotate(head):
            head_copy = head
            while head_copy.next.next is not None:
                head_copy = head_copy.next
            
            final = head_copy.next
            head_copy.next = None
            return final 
        
        while k > 0:
            var = rotate(head)
            var.next = head
            head = var
            k -= 1 

        return head


example = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

obj = Solution()
print(obj.rotateRight(example, 2))
