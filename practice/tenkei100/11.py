from itertools import product
N, M = map(int, input().split())

denkyuu = []
for i in range(M):
    den = list(map(int, input().split()))
    denkyuu.append(den)

jouken = list(map(int, input().split()))
ans = 0

for bit in product((0, 1), repeat=N):
    tenntou = [False for _ in range(M)]
    for i in range(M):
        tmp = 0
        den = denkyuu[i]
        for j in range(den[0]):
            x = den[j+1]
            if bit[x-1] == 1:
                tmp += 1
        if tmp % 2 == jouken[i]:
            tenntou[i] = True
    if False not in tenntou:
        ans += 1

print(ans)
