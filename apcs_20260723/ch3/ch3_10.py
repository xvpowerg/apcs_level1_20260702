class Queue:
    def __init__(self):
        self.my_quque = []
    def enqueue(self,data):
        self.my_quque.append(data)
    def dequeue(self):
        return self.my_quque.pop(0)
    def size(self):
        return len(self.my_quque)
people = ['Amy', 'David', 'Sean']
queue = Queue()
for p in people:
    queue.enqueue(p)
    print("加入enqueue:",p)
while queue.size():
    print("dequeue:",queue.dequeue())
