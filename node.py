class Node():

    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    def setLeft(self,node):
        self.left=node
    def setRight(self,node):
        self.right=node
