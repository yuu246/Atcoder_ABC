import heapq

N, M = map(int, input().split())
graph = []
for i in range(N+1):
    graph.append([])

for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

visited = [False] * (N+1)
dist = [-1] * (N+1)
dist[0] = 0
visited[0] = True
dist[1] = 0
Q = []
heapq.heappush(Q, (dist[1], 1))

while len(Q) > 0:
    d, x = heapq.heappop(Q)
    if visited[x]:
        continue
    else:
        visited[x] = True
        for (y, c) in graph[x]:
            if dist[y] == -1 or dist[y] > dist[x] + c:
                dist[y] = dist[x] + c
                heapq.heappush(Q, (dist[y], y))

for i in range(1, N+1):
    print(dist[i])
