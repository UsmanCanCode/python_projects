def merge(arr1, arr2):      # merge two array A and B into C by comparing A[i...k] to B[j....l]
    if (arr1 is None):
        return
    if arr2 is None:
        return

    arrayC = []

    i, j, k = 0,0,0

    while i < len(arr1) and j < len(arr2):

        if arr1[i] <= arr2[j]:
            arrayC.append(arr1[i])
            i+=1

        else:
            arrayC.append(arr2[j])
            j+=1

    while i < len(arr1):                # if exit while loop and still elements in either array add to C
        arrayC.append(arr1[i])
        i+=1

    while j < len(arr2):
        arrayC.append(arr2[j])
        j+=1

    return arrayC

def mergesort(array):
    if len(array)<2:
        return array
    middle = int(len(array)/2)

    left = array[:middle]
    right = array[middle:]

    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)


array = [2, 1]
sortedArray = mergesort(array)

print(sortedArray)





