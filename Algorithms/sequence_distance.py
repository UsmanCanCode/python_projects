'''See how close are two DNA sequence
    add cost p if it is a chain
    add cost q for each base in a chain
    return p and q
    example s1 = CTAAAAGC t1 = CTGC => p =1 q=4
    example s1 = CATAGACA t1 = CTGC => p =4 q=4
'''


def sequencedistance( s1, t1):

    if len(s1) == 0:
        return len(t1)
    if len(t1) == 0:
        return len(s1)

    p=[]
    q=[]

    i=0
    j=0
    #loop unlil either string is exahusted
    while i<len(s1) and j<len(t1):

        if s1[i] == t1[j]:
                i+=1
                j+=1
        else:
            #add cost if character not matching in source to target p
            p.append('p')
            while(s1[i] != t1[j]): #loop until a match is found while adding q cost

                q.append('q')
                i+=1
                if(i >= len(s1)):
                    break

    if(j == len(t1) and i != len(s1)):
        #if there are unmatched character add there cost .
        # p only added if previous character was a mtach and we have new chain
        if s1[i-1] == t1[-1]:
            p.append('p')

        for i in range((len(s1)-i)):
            q.append('q')


    return len(p), len(q)

s1 = 'CTAAAAGC'
s2 = 'CATAGACA'
t1 = 'CTGC'

print(sequencedistance(s2,t1))