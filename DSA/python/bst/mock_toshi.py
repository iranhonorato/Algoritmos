
class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#        0(a)
#       /     \
#     1(b)     1(c)
#    /         /
#   0(e)     1(d)
#  /    \
# 1(f) 1(g)
#  \       \
#   1(h)    1(i)

def count_islands_iran(root:Node) -> int:

    if root is None:
        return 0
    
    islands = [0]

    def dfs(node, is_island):
        if node is None:
            return

        elif node.val == 1:
            if is_island == False:
                is_island = True
                islands[0] += 1
                
        else:
            is_island = False

        dfs(node.left, is_island)
        dfs(node.right, is_island)
        return  
    
    dfs(root, False)
    return islands[0]



def count_islands_toshi(root:Node) -> int:
    if root is None:
        return 0 

    def dfs(node, is_island):
        islands = 0

        if node is None:
            return 0 

        elif node.val == 1:
            if is_island == False:
                is_island = True
                islands = 1 
        else:
            is_island = False

        islands += dfs(node.left, is_island)
        islands += dfs(node.right, is_island)
        return islands

    return dfs(root, False)


h = Node(1)
i = Node(1)

f = Node(1, right=h)
g = Node(1, right=i)

e = Node(0, left=f, right=g)
d = Node(1)

b = Node(1, left=e)
c = Node(1, left=d)

a = Node(0, left=b, right=c)

root = a

print(count_islands_iran(root))
print(count_islands_toshi(root))