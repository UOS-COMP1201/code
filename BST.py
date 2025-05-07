
from node import Node
class BST():
    def __init__(self,root=None):
        self.root=root
    def __insert(self,p,val):
        if p.val>val:
            if p.left==None:
                p.left=Node(val)
            else:
                self.__insert(p.left,val)
        else:
            if p.right==None:
                p.right=Node(val)
            else:
                self.__insert(p.right,val)
    def insert(self,val):
        if self.root==None:
            self.root=Node(val)
        else:
            self.__insert(self.root,val)
    def inorder(self):
       if self.root!=None:
          self.__inorder(self.root)
       print()
    def rinorder(self):
        if self.root!=None:
            self.__rinorder(self.root)
        print()
    def __inorder(self,root):
        if root == None:
            return
        self.__inorder(root.left)
        print(root.val,end=' ')
        self.__inorder(root.right)

    def __rinorder(self,root):
        if root == None: 
           return
        self.__rinorder(root.right)
        print(root.val,end=' ')
        self.__rinorder(root.left)
