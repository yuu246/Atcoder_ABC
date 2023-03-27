import sys

sys.setrecursionlimit(10**9)


def dfs(x):
    if not seen[x]:
        seen[x] = True
        for y in graph[x]:
            if not seen[y]:
                counter[y] += counter[x]
                dfs(y)


N, Q = map(int, input().split())
counter = [0] * (N+1)
seen = [True] + [False] * N
graph = [[] for _ in range(N+1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for _ in range(Q):
    a, b = map(int, input().split())
    counter[a] += b

dfs(1)
print(*counter[1:])
