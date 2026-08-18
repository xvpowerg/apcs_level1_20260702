def merge(left,right):
    output = []
    while left and right:
        if left[0] <= right[0]:
            output.append(left.pop(0))
        else:
            output.append(right.pop(0))
    if left:
        output += left
    if right:
        output += right
    return output

def mergeSort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    left  = mergeSort(left)
    right  = mergeSort(right)
    return merge(left,right)
data = [6,1,5,7,3,9,4]
print(data)
print(mergeSort(data))
