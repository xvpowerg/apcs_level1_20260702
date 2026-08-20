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
    def maxNode(self):
        ptr = self
        while  ptr.right:
            ptr = ptr.right
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
    def delete_l(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_l(val)
            else:
                print(val,"不存在")
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_l(val)
            else:
                print(val,"不存在")
        else:
            if not self.left:
                tmp = self.right
                self.data = Node
                return tmp
            elif not self.right:
                tmp = self.right
                self.data = None
                return tmp
            else:
                tmp = self.left.maxNode()
                self.data = tmp.data
                if self.left.data == tmp.data:
                    self.left = None
                else:
                    self.left.delete_l(tmp.data)
        return self            
bst = Node()
datas = [20,15,17,30,32,27,4]
for d in datas:
    bst.insert(d)
bst.inorder()
print()
#print(bst.maxNode())
n = int(input("輸入刪除資料"))
bst.delete_l(n)
bst.inorder()
print()

