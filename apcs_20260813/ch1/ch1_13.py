import  itertools
myList = [1,2,3,4,5,6,7,8,9]
perm_list = list(itertools.permutations(myList))
#print(perm_list[:6])
for i in perm_list:
    if i[0] / (i[1] *10  + i[2]) + i[3] / (i[4] * 10 +i[5])+ i[6]/(i[7]*10 + i[8]) == 1:
        print(f"{i[0]}      {i[3]}      {i[6]}")
        print(f"{i[1]}{i[2]}     {i[4]}{i[5]}    {i[7]}{i[8]}")
        print()
