def binarysearch(array, val, low, hi):
    if hi<low:
        return -1

    mid = int((low+hi)/2)

    if array[mid] > val:
        return binarysearch(array, val, low, mid-1)
    if array[mid] < val:
        return binarysearch(array, val, mid+1, hi)
    else:
        return mid



arraylist= [1,2,4,5,6,7,8,8,8,9,9,9,9,9,9,10,11,12,13,14,15,16,17,18,19,20]
val = 10

index = binarysearch(arraylist, val, 0, len(arraylist)-1)

print(index)
print(arraylist[index])