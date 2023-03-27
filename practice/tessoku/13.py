N = int(input())
menber = [0]*2 + list(map(int, input().split()))
graph = []
for _ in range(N+1):
    graph.append([])

for i in range(2, N+1):
    graph[menber[i]].append(i)

dp = [0] * (N+1)

for i in range(N, 0, -1):
    for j in graph[i]:
        dp[i] += dp[j] + 1

print(*dp[1:])
