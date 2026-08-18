def quickSort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst.pop(0)
    left = [i for i in lst if i < pivot]
    right = [i for i in lst if i >= pivot]
    return quickSort(left) + [pivot] + quickSort(right)
data = [6,1,5,7,3,9,4,2,8]
print(data)
print("排序完:",quickSort(data))
