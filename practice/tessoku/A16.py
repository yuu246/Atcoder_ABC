N = int(input())
A = [0, 0] + list(map(int, input().split()))
B = [0, 0, 0] + list(map(int, input().split()))


dp = [0 for i in range(N+1)]
dp[0] = 0
dp[1] = 0
dp[2] = A[2]
for i in range(3, N+1):
    dp[i] = min(dp[i-1] + A[i], dp[i-2] + B[i])

print(dp[N])
