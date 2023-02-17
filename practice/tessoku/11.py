import heapq

N, M = map(int, input().split())

graph = []
for _ in range(N+1):
    graph.append([])

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [-1] * (N+1)
dist[0] = 0

Q = []
heapq.heappush(Q, (1, 1))
dist[1] = 0

while len(Q) > 0:
    d, x = heapq.heappop(Q)
    for y in graph[x]:
        if dist[y] == -1 or dist[y] > dist[x] + 1:
            dist[y] = dist[x] + 1
            heapq.heappush(Q, (dist[y], y))

if dist[N] == 2:
    print('POSSIBLE')
else:
    print('INPOSSIBLE')
