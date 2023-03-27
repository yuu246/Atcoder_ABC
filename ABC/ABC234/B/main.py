#!/usr/bin/env python3

graph = []
N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    graph.append([x, y])

ans = -1
for i in range(N-1):
    for j in range(i+1, N):
        x1, y1 = graph[i]
        x2, y2 = graph[j]
        tmp = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        ans = max(tmp, ans)

print(ans)
