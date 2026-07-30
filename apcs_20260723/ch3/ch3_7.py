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
n1 = Node(5)
n2 = Node(15)
n3 = Node(25)
n1.next = n2
n2.next = n3
linke = Linked_list()
linke.head = n1
linke.print_list()
