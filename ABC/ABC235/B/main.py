#!/usr/bin/env python3
N = int(input())
H = list(map(int, input().split()))

ans = H[0]
for i in range(1, N):
    if H[i] > ans:
        ans = H[i]
    else:
        break

print(ans)
