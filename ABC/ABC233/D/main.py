#!/usr/bin/env python3
from collections import defaultdict

N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))
sum = [0 for _ in range(N+1)]
for i in range(1, N+1):
    sum[i] = sum[i-1] + A[i]

ans = 0
D = defaultdict()

for r in range(N+1):
    ans += D[sum[r]-K]
    D[sum[r]] += 1

print(ans)
