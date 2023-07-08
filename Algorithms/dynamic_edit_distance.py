def f(i, j, s1,s2, dp):
    print(f"in begining {i,j, dp[i][j]}")
    if(i<0):
        return j + 1
    if(j<0):
        return i + 1
    if(dp[i][j] != -1):
        return dp[i][j]
    if(s1[i] == s2[j]):
        dp[i][j] = f(i-1, j-1, s1,s2, dp)
        print(f"in middle {i, j, dp[i][j]}")
        return dp[i][j]
    dp[i][j] = 1 + \
               min(f(i-1, j, s1, s2,dp),
               min(f(i, j-1, s1, s2,dp), f(i-1, j-1, s1,s2,dp )))

    print(f"in end {i, j, dp[i][j]}")
    return  dp[i][j]


def editdistance (s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[-1 for i in range(m)] for j in range(n)]
    return f(n-1, m-1, s1,s2 , dp)


def editdistanceloop(s1, t1):

    #if source is empty and if target is empty
    if (len(s1) == 0):
        return len(t1)
    if(len(t1) == 0):
        return len(s1)

    len_s1 = len(s1)
    len_t1 = len(t1)
    cost = 0
    for i in range(0, len_s1):
        for j in range(i, len_t1):

            print(s1[i], t1[j])



s1 = 'CTGC'
s2 = 'CTAAAAGC'

print(editdistance(s1,s2))