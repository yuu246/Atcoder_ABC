from collections import deque

N, M = map(int, input().split())
graph = [list() for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

mod = 10**9+7

visited = [-1 for i in range(N+1)]
keiro = [0 for i in range(N+1)]
keiro[1] = 1
visited[1] = 0

Q = deque()
Q.append(1)

while len(Q) > 0:
    x = Q.popleft()
    for y in graph[x]:
        if visited[y] == -1:
            visited[y] = visited[x] + 1
            keiro[y] = keiro[x]
            Q.append(y)
        else:
            if visited[y] == visited[x] + 1:
                keiro[y] += keiro[x]
        keiro[y] %= mod

print(keiro[N])
