from collections import deque

N, M = map(int, input().split())

graph = []
for i in range(N+1):
    graph.append([])
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [-1]*(N+1)
Q = deque([])
Q.append(1)
visit[1] = 0

while len(Q) > 0:
    x = Q.popleft()
    for y in graph[x]:
        if visit[y] == -1:
            visit[y] = visit[x] + 1
            Q.append(y)

for i in range(1, N + 1):
    print(visit[i])
