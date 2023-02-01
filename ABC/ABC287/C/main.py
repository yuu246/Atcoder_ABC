#!/usr/bin/env python3
from collections import deque

N, M = map(int, input().split())

if N-1 != M:
    print('No')
else:
    graph = []
    for _ in range(N):
        graph.append([])

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    visited = []
    for _ in range(N):
        visited.append(False)
    
    Q = deque()
    Q.append(0)
    count = 0

    while 0 < len(Q) < 3:
        x= Q.popleft()

        if visited[x]:
            break

        visited[x] = True
        count += 1
        for i in graph[x]:
            if not visited[i]:
                Q.append(i)

    if count == N:
        print('Yes')
    else:
        print('No')



