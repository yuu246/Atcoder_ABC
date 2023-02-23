H, W = map(int, input().split())
graph = [[]]
for _ in range(H):
    X = [0] + list(map(int, input().split()))
    graph.append(X)

sum_graph = [[0] * (W+1) for _ in range(H+1)]
for i in range(1, H+1):
    for j in range(1, W+1):
        sum_graph[i][j] = sum_graph[i][j-1] + graph[i][j]

for j in range(1, W+1):
    for i in range(1, H+1):
        sum_graph[i][j] = sum_graph[i-1][j] + sum_graph[i][j]

Q = int(input())

for i in range(Q):
    a, b, c, d = map(int, input().split())
    ans = sum_graph[c][d] + sum_graph[a-1][b-1] - \
        sum_graph[c][b-1] - sum_graph[a-1][d]
    print(ans)
