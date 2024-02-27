

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

    soretedArray = sorted(array)

     




print(arrayTwoSum(array2, 3))
