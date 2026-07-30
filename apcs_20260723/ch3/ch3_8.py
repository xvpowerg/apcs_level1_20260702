class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)
class Linked_list():
    def __init__(self):
        self.head = None
    def print_list(self):
        ptr = self.head
        while ptr:
            print(ptr)
            ptr = ptr.next
    def add(self,item):
        newNode = Node(item)
        if  self.head == None:
            self.head = newNode
            return
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = newNode
linke = Linked_list()
data = [5,15,25]
for v in data:
    linke.add(v)
    
linke.print_list()
