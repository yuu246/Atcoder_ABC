#!/usr/bin/env python3

N = int(input())
Timer = [0] + list(map(int, input().split()))

all = sum(Timer)
dp = []
for i in range(N+1):
    dp.append([False] * (all+1))

dp[0][0] = True

for i in range(1, N+1):
    for j in range(all+1):
        if dp[i-1][j]:
            dp[i][j] = True
        if j-Timer[i] >= 0:
            if dp[i-1][j-Timer[i]]:
                dp[i][j] = True

for i in range(-(-all//2), all+1):
    if dp[N][i]:
        print(i)
        break
