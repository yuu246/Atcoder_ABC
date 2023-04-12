from itertools import product

H, W = map(int, input().split())

graph = []
for i in range(H):
    A = list(map(int, input().split()))
    graph.append(A)
ans = 0
for bit in product((0, 1), repeat=H+W-2):
    if sum(bit) != W-1:
        continue
    tmp = set()
    i, j = 0, 0
    tmp.add(graph[i][j])
    for x in bit:
        if x == 1:
            j += 1
            tmp.add(graph[i][j])
        else:
            i += 1
            tmp.add(graph[i][j])
    if len(tmp) == H + W - 1:
        ans += 1
print(ans)
