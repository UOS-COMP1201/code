class Node():

    def __init__(self,val,parent=None,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
        self.parent=parent
    def setLeft(self,node):
        self.left=node
    def setRight(self,node):
        self.right=node
    def setParent(self,node):
        self.parent=node
