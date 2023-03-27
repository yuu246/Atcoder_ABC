#!/usr/bin/env python3

N, X = map(int, input().split())
a = []
b = []
for i in range(N):
    A, B = map(int, input().split())
    a.append(A)
    b.append(B)

dp = [[False for _ in range(X+1)] for _ in range(N+1)]
dp[0][0] = True

for i in range(N):
    for j in range(X+1):
        for k in range(b[i]+1):
            if dp[i][j] and j+a[i]*k<=X:
                dp[i+1][j+a[i]*k] = True
if dp[N][X]:
    print("Yes")
else:
    print("No")