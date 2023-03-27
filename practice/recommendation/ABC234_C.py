import heapq
N, K = map(int, input().split())
P = list(map(int, input().split()))

que = []

for i in range(K):
    heapq.heappush(que, P[i])

print(que[0])

for idx in range(K, N):
    x = heapq.heappop(que)
    heapq.heappush(que, max(x, P[idx]))
    print(que[0])
