#!/usr/bin/env python3

import sys
sys.setrecursionlimit(100000)

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append([])

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * N
ans = 0

def dfs(x, y):
    if visited[y]:
        return
    else:
        for z in graph[y]:
            if z == x:
                continue
            else:
                if visited[z]:
                    global ans 
                    ans += 1
                    visited[y] = True
                    return
                else:
                    visited[y] = True
                    dfs(y, z)

for x in range(N):
    if not visited[x]:
        for y in graph[x]:
            if not visited[y]:
                visited[x] = True
                dfs(x, y)

print(ans)
