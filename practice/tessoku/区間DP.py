N = int(input())
P = [0]
A = [0]
for i in range(N):
    p, a = map(int, input().split())
    P.append(p)
    A.append(a)

dp = []
for i in range(N+1):
    tmp = [None]*(N+1)
    dp.append(tmp)

dp[1][N] = 0
for right in range(N, 0, -1):
    for left in range(1, right+1):

        score1 = 0
        if left >= 2 and left <= P[left-1] <= right:
            score1 = A[left-1]

        score2 = 0
        if right <= N-1 and left <= P[right+1] <= right:
            score2 = A[right+1]

        if left == 1 and right == N:
            continue
        elif left == 1:
            dp[left][right] = dp[left][right+1] + score2
        elif right == N:
            dp[left][right] = dp[left-1][right] + score1
        else:
            dp[left][right] = max(dp[left-1][right] +
                                  score1, dp[left][right+1] + score2)

ans = 0
for i in range(1, N+1):
    ans = max(ans, dp[i][i])
print(ans)
