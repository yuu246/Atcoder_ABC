N, S = map(int, input().split())
A = [0]
a = list(map(int, input().split()))
A = A + a

dp = []
for i in range(N+1):
    tmp = [False] * (S+1)
    dp.append(tmp)

dp[0][0] = True
for i in range(1, N+1):
    num = A[i]
    for j in range(0, S+1):
        if j < num:
            if dp[i-1][j]:
                dp[i][j] = True
        else:
            if dp[i-1][j-num] or dp[i-1][j]:
                dp[i][j] = True
 
if dp[N][S]:
    print('Yes')
else:
    print('No')