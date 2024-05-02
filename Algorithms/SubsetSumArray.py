

array = [5,2,6,10]
array2 = [5,2,4,3,6,12]


def arrayTwoSum(array, target):
    '''
    Find a 2 numbers in array whose sum equals target

    example :
        given array [ 5,2,6,10]
        target = 12
        return Yes or [2,10]
    '''

    currentSum = 0

    subset = []
    ans =[]

    for i in range(len(array)):
        if array[i] == target:
            ans.append(array[i])
            return True, ans
        if array[i] in subset:
            ans.append(array[i])
            ans.append((target-array[i]))
            return True, ans
        else:
            complement = target - array[i]
            subset.append(complement)


    return False


def subsetSum(array, Target):
    '''
    given a array of integers find a subset whose sum equals target
    example:
    array = [5,2,6,10]
    target = 13
    return True or susbet = [ 5,2,6]
    :param array: integers
    :param Target: integer
    :return: True or actual subset
    '''

    def take_or_not(arr, length, target):

        if target == 0:
            return True

        if length == 0:
            if target - array[length] == 0:
                return True
            else:
               return False


        return take_or_not(arr, length-1, target-arr[length-1]) or \
                take_or_not(arr, length-1, target)

    return take_or_not(array, len(array), Target)

def isSubsetSum(set, n, sum):

    # Base Cases
    if (sum == 0):
        return True
    if (n == 0):
        return False

    # If last element is greater than
    # sum, then ignore it
    if (set[n - 1] > sum):
        return isSubsetSum(set, n - 1, sum)

    # Else, check if sum can be obtained
    # by any of the following
    # (a) including the last element
    # (b) excluding the last element
    return isSubsetSum(
        set, n-1, sum) or isSubsetSum(
        set, n-1, sum-set[n-1])

array = [3, 34, 4, 12, 5, 2]

print(isSubsetSum(array, 6, 13))

print(arrayTwoSum(array2, 3))
