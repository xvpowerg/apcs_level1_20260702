def partition(a,left,right):
    S = a[left]
    i,j = left + 1,right
    while True:
        while i <= right and a[i] <= S:
            i += 1
        while j >= left+1 and a[j] >= S:
            j -= 1
        if i < j:
            a[i],a[j] = a[j],a[i]
        else:
            break
    a[left],a[j] = a[j],a[left]
    return j
def quicksort(a,left,right):
    if left >= right:
        return
    p = partition(a,left,right)
    quicksort(a,left,p-1)
    quicksort(a,p+1,right)
arr = [30, 24, 27, 16, 29, 33, 25, 18, 32, 35]
quicksort(arr,0,len(arr) - 1)
print(arr)
    
