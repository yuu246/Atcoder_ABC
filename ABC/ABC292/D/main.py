#!/usr/bin/env python3

from collections import deque


def dfs(Q):
    visit_count = 0
    add_count = 0
    while len(Q) > 0:
        x = Q.pop()
        if not visited[x]:
            visited[x] = True
            visit_count += 1
            for y in graph[x]:
                if x == y:
                    add_count += 1
                if not visited[y]:
                    Q.append(y)
                    add_count += 1
        else:
            continue
    if visit_count == add_count:
        return True
    else:
        return False


N, M = map(int, input().split())

if N != M:
    print('No')
else:
    graph = [[]]
    for i in range(N):
        graph.append([])

    for i in range(M):
        u, v = map(int, input().split())
        if u == v:
            graph[u].append(v)
        else:
            graph[u].append(v)
            graph[v].append(u)

    visited = [True] + [False] * (N)
    Q = deque()
    for i in range(1, N+1):
        if not visited[i]:
            Q.append(i)
            if dfs(Q):
                continue
            else:
                print('No')
                break
    else:
        print('Yes')
