# i = A[i]

def index_equal_element(array, low, high):
    if high < low:
        return False

    mid = int(low + high/2)

    if array[mid] == mid:
        return True
    elif array[mid] > mid:
        return index_equal_element(array, low, mid-1)

    elif array[mid] < mid:
        return index_equal_element(array, mid+1, high)



A = [1, 3, 4, 5]

print(index_equal_element(A, 0, len(A)-1))