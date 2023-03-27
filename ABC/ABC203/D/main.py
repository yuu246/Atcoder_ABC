#!/usr/bin/env python3

N, K = map(int, input().split())
if K % 2 == 0:
    X = K**2 // 2 - 1
else:
    X = K**2 // 2

graph = []
for i in range(N):
    A = list(map(int, input().split()))
    graph.append(A)

separate = []
for i in range(N-K+1):
    separate.append([0]*(N-K+1))


for i in range(0, N-K+1):
    for j in range(0, N-K+1):
        tmp = []
        for k in range(i, i+K):
            B = graph[k][j:j+K]
            tmp += B
        tmp.sort()
        separate[i][j] = tmp[X]

ans = 10*10
for i in range(0, N-K+1):
    ans = min(separate[i])
print(ans)
