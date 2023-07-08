def checkbad(element):
    if element == 'B':
        return True
    return False


def checkfirstbad(array, low, high):

    if high < low:
        if checkbad(array[0]):
            return 0
        return -1

    mid  = int((high+low)/2)

    if checkbad(array[mid]):
        if not checkbad(array[mid - 1]):
            return mid
        else:
            return checkfirstbad(array, low, mid-1)
    else:
        return checkfirstbad(array, mid+1, high)

g = 'G'
b = 'B'
array = [g,g,g,g,g,b]
index = checkfirstbad(array, 0, len(array)-1)

print(index)
