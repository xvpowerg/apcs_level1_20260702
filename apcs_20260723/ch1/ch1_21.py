class Point:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
    def __str__(self):#定義如何轉成字串
        return f"({self.x},{self.y})"
    def __lt__(self,other):
        self_len = self.x ** 2 + self.y ** 2
        other_len = other.x ** 2 +other.y ** 2
        return self_len < other_len
    def __eq__(self,other):
        self_len = self.x ** 2 + self.y ** 2
        other_len = other.x ** 2 +other.y ** 2
        return self_len == other_len
    
p1 = Point(1,2)
p2 = Point(9,8)
p3 = Point(1,2)
print(p1 < p2)
print(p1 > p2)
print(p1 == p3)
