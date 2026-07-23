def test1(a):
    print("S:",a)
    if a < 5:
        test1(a + 1)
    print("E:",a)     
        
test1(1)    
