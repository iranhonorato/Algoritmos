from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def kth_from_last_it(head: Optional[ListNode], k:int) -> Optional[ListNode]:
    if head is None or k <= 0:
        return None
    
    size = 0
    node = head
    while node:
        node = node.next    
        size += 1 

    if k > size:
        return None

    target = size - k 

    node = head
    for i in range(target):
        node = node.next

    return node 


def kth_from_last_rec(head: Optional[ListNode], k:int) -> Optional[ListNode]:
    ans = None 
    count = k

    def recursion(node):
        nonlocal ans, count

        if node is None:
            return 

        recursion(node.next, count)
        count -= 1 

        if count == 0:
            ans = node 
        return
    
    recursion(head, k)
    return ans