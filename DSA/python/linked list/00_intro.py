# Definição

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



a = ListNode(1, 
             ListNode(2, 
                      ListNode(3, None)))
b = ListNode(1, 
             ListNode(4, 
                      ListNode(5, None)))

