N = int(input())
P = [0] + list(map(int, input().split()))
max = sum(P)
dp = [[False] * (max+1) for i in range(N+1)]
dp[1][0] = True
dp[1][P[1]] = True
for i in range(2, N+1):
    for j in range(max+1):
        if j == 0:
            dp[i][j] = True
        if dp[i-1][j]:
            dp[i][j] = True
        if j - P[i] >= 0 and dp[i-1][j-P[i]]:
            dp[i][j] = True

ans = sum(dp[N])
print(ans)
