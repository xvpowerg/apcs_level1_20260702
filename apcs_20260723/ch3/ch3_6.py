class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)
n1 = Node(5)
n2 = Node(15)
n3 = Node(25)
#Linked
lsp = n1
n1.next = n2
n2.next = n3
while lsp:
    print(lsp)
    lsp = lsp.next
