def get_sum(a,b):
    return a + b
#return 離開函式

def test_run(a):
    for i in range(1,6):
        print("i:",i)
        if i == a:
            #break#離開回圈
            return#離開函式 要放在函式 可放在迴圈之外
    print("func完成")    

print(get_sum(5,2))
test_run(3)
