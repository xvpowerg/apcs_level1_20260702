class Student:
    className = "甲班"
    def __init__(self,name,score=0):
        self.name = name
        self.score = score
    def printInfo(self):
        print(self.name,self.score,Student.className)
st1 = Student("Ken",20)
st2 = Student("Iris",18)
Student.className = "乙班"
stList = [st1,st2]
for st in stList:
    st.printInfo()
