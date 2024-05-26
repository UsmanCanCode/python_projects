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


def searchbinary(array, target):

    hi = len(array)-1
    lo = 0
    mid = int((hi+lo)/2)

    while hi >= lo:
        mid = int((lo + hi) / 2)
        if array[mid] > target:
            hi = mid-1
        elif array[mid] < target:
            lo = mid + 1
        elif array[mid] == target:
            return mid

    return -1




arraylist= [1,2,4,5,6,7,8,8,8,9,9,9,9,9,9,9,10,11,12,13,14,16,17,18,19]
val = 10


index = searchbinary(sorted(arraylist), val)

print(index)
print(arraylist[index])