S = 'A' + input()
T = 'Dchokudai'
dp = [[0 for _ in range(len(T))] for i in range(len(S))]
mod = 1000000007

for i in range(len(S)):
    for j in range(len(T)):
        if j == 0:
            dp[i][j] = 1
            continue
        if S[i] == T[j]:
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j]
        dp[i][j] %= mod


ans = dp[len(S)-1][len(T)-1]

print(ans)
