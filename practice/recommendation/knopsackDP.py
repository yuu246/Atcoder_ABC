N, W = map(int, input().split())
weight = [0]
value = [0]
dp = [[0] * (W+1) for i in range(N+1)]
for _ in range(N):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

dp[1][weight[1]] = value[1]
for i in range(2, N+1):
    for j in range(1, W+1):
        if j - weight[i] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i])
        else:
            dp[i][j] = dp[i-1][j]
ans = max(dp[N])
print(ans)
