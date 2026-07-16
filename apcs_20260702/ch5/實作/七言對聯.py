n = int(input())                            #對聯數量
antiRule = []                               #違反規則list
for _ in range(n):
    s1 = list(map(int, input().split()))    #上聯
    s2 = list(map(int, input().split()))    #下聯
    if (s1[1]==s1[3]) | (s1[1]!=s1[5]) | (s2[1]==s2[3]) | (s2[1]!=s2[5]):
        antiRule.append("A")                #違反規則A
    if (s1[6] != 1) | (s2[6] != 0):         
        antiRule.append("B")                #違反規則B
    if (s1[1]==s2[1]) | (s1[3]==s2[3]) | (s1[5] == s2[5]):
        antiRule.append("C")                #違反規則C
    #列印所有違反的規則,antiRule為空,列印None
    print("".join(antiRule)) if antiRule != [] else print("None") 
    antiRule = []                           #清空antiRule
