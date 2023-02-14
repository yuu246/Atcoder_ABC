N, W = map(int, input().split())

dp = []
for _ in range(N+1):
    tmp = [0]*(W+1)
    dp.append(tmp)

Weigt = [0]
Value = [0]
for _ in range(N):
    w, v = map(int, input().split())
    Weigt.append(w)
    Value.append(v)

for i in range(1, N+1):
    for j in range(W+1):
        if j < Weigt[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-Weigt[i]]+Value[i], dp[i-1][j])

print(max(dp[N]))
