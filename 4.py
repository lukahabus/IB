def maxPairs(N, P, A):
    pairs = 0

    for row in A:
        dogs = []
        cats = []

        for i in range(len(row)):
            if row[i] == "D":
                dogs.append(i)
            elif row[i] == "C":
                cats.append(i)

        for dog in dogs:
            for cat in cats:
                if abs(cat - dog) <= P:
                    pairs += 1
                    cats.remove(cat)
                    break

    return pairs


N, P = map(int, input().split())

A = []
for i in range(N):
    A.append(input().split())

print(maxPairs(N, P, A))
