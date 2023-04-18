def sumHeight(Q,L,R):
    # this is default OUTPUT. You can change it.
    result = 0
    stablo = [1] * 100001

    # write your Logic here:
    for i in range(Q):
        for j in range(L[i], R[i] + 1):
            stablo[j] = 0

    for i in range(100001):
        if stablo[i] == 1:
            result += i
    
    return result


# INPUT [uncomment & modify if required]
Q = int(input())

L = []
R = []
for i in range(Q):
    l,r = input().split()
    L.append(int(l))
    R.append(int(r))

# OUTPUT [uncomment & modify if required]
print(sumHeight(Q, L, R))