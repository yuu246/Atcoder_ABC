from collections import deque

N, M = map(int, input().split())
graph = []
for i in range(N+1):
    graph.append([])
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
visited[0] = True

Q = deque()
Q.append(1)

while len(Q) > 0:
    x = Q.pop()
    if visited[x]:
        continue
    else:
        visited[x] = True
        for y in graph[x]:
            Q.append(y)


if False not in visited:
    print('The graph is connected.')
else:
    print('The graph is not connected.')
