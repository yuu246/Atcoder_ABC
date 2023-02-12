H, W = map(int, input().split())

graph = []
for i in range(H):
    v = list(map(int, input().split()))
    graph.append(v)

sum_graph = []
for i in range(H):
    sum_graph.append([0]*W)


for i in range(H):
    for j in range(W):
        if i == 0 and j ==0:
            sum_graph[0][0] = graph[0][0]
        else:
            sum_graph[i][j] = sum_graph[i][j-1] + graph[i][j]

sum2_graph = []
for i in range(H):
    sum2_graph.append([0]*W)

for j in range(W):
    for i in range(H):
        if i == 0 and j ==0:
            sum2_graph[0][0] = sum_graph[0][0]
        else:
            sum2_graph[i][j] = sum2_graph[i-1][j] + sum_graph[i][j]


Q = int(input())
for _ in range(Q):
    tmp = 0
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1

    if a == 0 and b != 0:
        ans = sum2_graph[c][d] - sum2_graph[c][b-1]
    elif a != 0 and b == 0:
        ans = sum2_graph[c][d] - sum2_graph[a-1][d]
    elif a==0 and b == 0:
        ans = sum2_graph[c][d]
    elif a!=0 and b!=0:
        ans = sum2_graph[c][d] + sum2_graph[a-1][b-1] - sum2_graph[a-1][d] - sum2_graph[c][b-1]

    print(ans)
