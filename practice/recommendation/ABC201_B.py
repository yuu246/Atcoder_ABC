import heapq
Q = []
N = int(input())
for i in range(N):
    S, T = map(str, input().split())
    T = int(T) * -1
    heapq.heappush(Q, [T, S])

for i in range(2):
    t, s = heapq.heappop(Q)
    if i == 1:
        print(s)
