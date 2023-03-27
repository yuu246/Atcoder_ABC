from itertools import product
N, M = map(int, input().split())

C = [[i] for i in range(N)]
for i in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    C[x].append(y)
    C[y].append(x)

ans = 0
for bit in product([0, 1], repeat=N):
    flag = 1
    cone_kouho = []
    for i in range(N):
        if bit[i] == 1:
            cone_kouho.append(i)
    cone_kouho = set(cone_kouho)
    for i in cone_kouho:
        for j in cone_kouho:
            if j not in C[i]:
                flag = 0
    if flag:
        ans = max(ans, len(cone_kouho))

print(ans)
