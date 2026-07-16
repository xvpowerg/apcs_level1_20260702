a, b, c = map(int, input().split())  #切割輸入字串

#將大於0的a b值轉換為1
a = 1 if a!=0 else 0 
b = 1 if b!=0 else 0

#運算符號運算結果為c時印出該運算符號
if (a and b) == c:  # a and b 運算結果是否為c
    print("AND")
if (a or b) == c:   # a or b 運算結果是否為c
    print("OR")
if (a ^ b) == c:    # a xor b 運算結果是否為c
    print("XOR")  
#三個運算符號均無法取得該結果列印"IMPOSSIBLE"
if (a and b) != c and (a or b) != c and (a ^ b) != c:
    print("IMPOSSIBLE")
