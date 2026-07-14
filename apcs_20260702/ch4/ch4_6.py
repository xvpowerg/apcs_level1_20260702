a = 2
def func():
    global a #宣告a變數為外部的a
    a = 10
    print("func():",a)
    
print("test1:",a)
func()
print("test2:",a)
