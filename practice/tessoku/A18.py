N, S = map(int, input().split())
A_list = [0] + list(map(int, input().split()))

dp = [[False for i in range(S+1)] for i in range(N+1)]


dp[0][0] = True
for i in range(1, N+1):
    for s in range(S+1):
        if s - A_list[i] >= 0:
            if dp[i-1][s-A_list[i]] or dp[i-1][s]:
                dp[i][s] = True
        else:
            if dp[i-1][s]:
                dp[i][s] = True


if dp[N][S]:
    print('Yes')
else:
    print('No')
