import math


def setsOfBalls(N, P, Q):
    result = 0

    for i in range(1, N + 1):
        result += math.comb(N, i) if i != P and i != Q else 0
        # print(i, math.comb(N,i))

    return result


# INPUT [uncomment & modify if required]
N = int(input())

P, Q = input().split()
P = int(P)
Q = int(Q)

# OUTPUT [uncomment & modify if required]
print(setsOfBalls(N, P, Q))
