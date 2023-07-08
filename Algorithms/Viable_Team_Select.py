# Team  x   y
# T1    0   2
# T2    1   8
# T3    2   7
# T4    8   5

def mergeTeam(arr1, arr2):

    if arr1 is None:
        if arr2 is None:
            return
        else:
            return arr2
    if arr2 is None:
        if arr1 is None:
            return
        else:
            return arr1

    arrC = []

    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):

        if arr1[i].get('x') > arr2[j].get('x') and arr1[i].get('y') > arr2[j].get('y'):
            arrC.append(arr1[i])
            i += 1
            j += 1
        elif arr2[j].get('x') > arr1[i].get('x') and arr2[j].get('y') > arr1[i].get('y'):
            arrC.append(arr2[j])
            i += 1
            j += 1
        elif arr1[i].get('x') > arr2[j].get('x'):
            arrC.append(arr2[j])
            j += 1
        else:
            arrC.append(arr1[i])
            i += 1

    while i < len(arr1):
        arrC.append(arr1[i])
        i += 1
    while j < len(arr2):
        arrC.append(arr2[j])
        j += 1

    return arrC


def sortTeam(arr):
    if len(arr)<2:
        return arr

    mid = int(len(arr)/2)

    left = arr[:mid]
    right = arr[mid:]

    left = sortTeam(left)
    right = sortTeam(right)

    return mergeTeam(left, right)


t1= {'x': 10, 'y':9}
t2= {'x': 1, 'y':11}
t3= {'x': 12, 'y':9}
t4= {'x': 10, 'y':12}

A = [t1, t2, t3, t4]

vteam = sortTeam(A)
print(vteam)

