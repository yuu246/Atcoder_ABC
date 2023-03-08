#!/usr/bin/env python3

from collections import Counter

N = int(input())
A = list(map(int, input().split()))
C = Counter(A)

ans = 0
for i in range(N):
    tmp_C = Counter(A[:i])
    ans += N - i - (C[A[i]] - tmp_C[A[i]])

print(ans)
