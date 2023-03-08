from itertools import product
N = int(input())
S = list(map(int, input()))

ans = 0
for q in product(range(10), repeat=3):
    i = 0
    for s in S:
        if s == q[i]:
            if i == 2:
                ans += 1
                break
            else:
                i += 1

print(ans)
