#!/usr/bin/env python3
from collections import deque
N, M = map(int, input().split())

graph = []
for i in range(N+1):
    graph.append([])

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)


def bfs(start):
    end = set()
    Q = deque()
    Q.append(start)
    while len(Q) > 0:
        x = Q.popleft()
        end.add(x)
        for y in graph[x]:
            if y not in end:
                Q.append(y)
    return len(end)


ans = 0
for i in range(1, N+1):
    ans += bfs(i)
print(ans)
