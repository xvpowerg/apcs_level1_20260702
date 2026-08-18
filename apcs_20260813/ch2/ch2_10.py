def combine(lst,n):

    if (lst) == n:
        return [lst]
    elif n == 1:
        return [[x] for x in lst]
    else:
        out = []
        for i in range(len(lst) - n + 1):
            first = lst[i]
            tails = combine(lst[i+1:],n-1)
            for c in  tails:
                out.append([first] + c)
        return out    
myList = combine([1,2,3,4,5,6],4)
for l in myList:
    print(l)
