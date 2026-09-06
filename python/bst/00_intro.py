# Definição


class Tree():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



a = Tree(5,
         Tree(3,Tree(1), Tree(4)), 
         Tree(7,Tree(6), Tree(8)))



def pre_order(a):
    if a is None:
        return
    
    print(a.val)
    pre_order(a.left)
    pre_order(a.right)

    return


def in_order(a):
    if a is None:
        return
        
    pre_order(a.left)
    print(a.val)
    pre_order(a.right)

    return


def post_order(a):
    if a is None:
        return
    
    pre_order(a.left)
    pre_order(a.right)
    print(a.val)

    return
