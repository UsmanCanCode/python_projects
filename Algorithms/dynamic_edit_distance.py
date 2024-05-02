
'''Recursive approach with memoization
    time complexity of O(m * n)
'''
def f(i, j, s1,s2, dp):

    if(i<0):
        return j + 1
    if(j<0):
        return i + 1
    if(dp[i][j] != -1):
        return dp[i][j]
    if(s1[i] == s2[j]):
        dp[i][j] = f(i-1, j-1, s1,s2, dp)

        return dp[i][j]
    dp[i][j] = 1 + \
               min(f(i-1, j, s1, s2,dp),
               min(f(i, j-1, s1, s2,dp), f(i-1, j-1, s1,s2,dp )))

    
    return  dp[i][j]


def editdistance (s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[-1 for i in range(m)] for j in range(n)]
    return f(n-1, m-1, s1,s2 , dp)



'''
Iterative approach of creating a 2d Dp Array
time complexity O(m * n)
'''


def editdistanceloop(s1, t1):

    #if source is empty and if target is empty
    if (len(s1) == 0):
        return len(t1)
    if(len(t1) == 0):
        return len(s1)

    len_s1 = len(s1)
    len_t1 = len(t1)
    cost = 0

    dp = [[-1 for j in range(0,len_s1 +1)] for i in range(0,len_t1+1)]
    for j in range(0,len_s1+1):
        dp[0][j] = len(s1[:j])

    for i in range(0, len_t1+1):
        dp[i][0] = len(t1[:i])

    print(dp)

    for i in range(1, len_t1+1):
        for j in range(1, len_s1+1):

                if s1[j-1] == t1[i-1]:
                    dp[i][j] = dp[i-1][j-1]




                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1]))

    print(dp)
    return dp[i][j]


s1 = 'Horse'
s2 = 'Ros'

print(editdistanceloop(s1,s2))