import heapq

N, M = map(int, input().split())
graph = [list() for i in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

INF = 10**9
kakutei = [False for i in range(N+1)]
zantei = [INF for i in range(N+1)]
zantei[1] = 0
Q = []
heapq.heappush(Q, (zantei[1], 1))

while len(Q) > 0:
    x = heapq.heappop(Q)[1]
    if kakutei[x]:
        continue

    kakutei[x] = True
    for y in graph[x]:
        next = y[0]
        cost = y[1]
        if zantei[next] > zantei[x] + cost:
            zantei[next] = zantei[x] + cost
            heapq.heappush(Q, ((zantei[next]), next))


for i in range(1, N+1):
    if zantei[i] != INF:
        print(zantei[i])
    else:
        print(-1)
