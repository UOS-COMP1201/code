import queue

class Node(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
    def children(self):
        return((self.left, self.right))

# freq = [
#    (8.167, 'a'), (1.492, 'b'), (2.782, 'c'), (4.253, 'd'),
#    (12.702, 'e'),(2.228, 'f'), (2.015, 'g'), (6.094, 'h'),
#    (6.966, 'i'), (0.153, 'j'), (0.747, 'k'), (4.025, 'l'),
#    (2.406, 'm'), (6.749, 'n'), (7.507, 'o'), (1.929, 'p'), 
#    (0.095, 'q'), (5.987, 'r'), (6.327, 's'), (9.056, 't'), 
#    (2.758, 'u'), (1.037, 'v'), (2.365, 'w'), (0.150, 'x'),
#    (1.974, 'y'), (0.074, 'z') ]
freq = [
    (25,'a'), (24, 'b'), (28, 'c'), (18, 'd'),(5, 'e')]

def create_tree(frequencies):
    p = queue.PriorityQueue()
    for value in frequencies:    # 1. Create a leaf node for each symbol
        p.put(value)             #    and add it to the priority queue
    while p.qsize() > 1:         # 2. While there is more than one node
        l, r = p.get(), p.get()  # 2a. remove two highest nodes
        node = Node(l, r) # 2b. create internal node with children
        p.put((l[0]+r[0], node)) # 2c. add new node to queue      
    return p.get()               # 3. tree is complete - return root node


# Recursively walk the tree down to the leaves,
#   assigning a code value to each symbol

def walk_tree(node, prefix=""):

     if isinstance(node[1],Node):
         l,r=node[1].children()
         walk_tree(l,prefix+"1")
         walk_tree(r,prefix+"0")
     else:
         code[node[1]]=prefix

node = create_tree(freq)
code={}
walk_tree(node)
print(code)
