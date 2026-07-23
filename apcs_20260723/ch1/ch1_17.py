class Employee:
    def __init__(self,name,age=0):
        self.name = name
        self.age = age
        print("__init__")
    def printInfo(self):
        print("emp:",self.name,self.age)
        
        
emp1 = Employee("Ken",25)
print(emp1.name,emp1.age)
emp2 = Employee("Iris",30)
print(emp2.name,emp2.age)
emp3 = Employee("Lucy")
print(emp3.name,emp3.age)
emp3 = Employee("Tom",12)
emp3.printInfo()
