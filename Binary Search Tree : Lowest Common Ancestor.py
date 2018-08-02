#https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
                    
def lca(root, v1, v2):
    #Enter your code here
    v1s, v2s = sorted([v1,v2])
    while not (v1s <= root.info <= v2s):
        if (v1s <= root.info):
            root = root.left
        else:
            root = root.right
    return root
tree = BinarySearchTree()
t = int(raw_input())

arr = list(map(int, raw_input().split()))

for i in xrange(t):
    tree.create(arr[i])
    
v = list(map(int, raw_input().split()))

ans = lca(tree.root, v[0], v[1])
print ans.info
