#!/usr/bin/env python3
from collections import deque

ans = 0

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append([])
for i in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

visited = [False] * N
next = deque([])

f = True
while f:
    if False not in visited:
        break
    else:
        idx = visited.index(False)
        next.append(idx)
        ans += 1

        while len(next) > 0:
            x = next.popleft()
            if visited[x]:
                continue
            else:
                visited[x] = True
                for y in graph[x]:
                    next.append(y)

print(ans)
