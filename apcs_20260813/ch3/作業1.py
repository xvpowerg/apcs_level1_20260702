class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data# 建立根節點
    def minNode(self):
        ptr = self
        while  ptr.left:
            ptr = ptr.left
        return ptr    
    def preorder(self):
        print(self.data,end="->")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data,end="->")
        if self.right:
            self.right.inorder()

bst = Node()
datas = [20,15,17,30,32,27,4]
for d in datas:
    bst.insert(d)
bst.inorder()
print()
print(bst.minNode())
