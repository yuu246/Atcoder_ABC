#!/usr/bin/env python3
N = int(input())

A_list = list(map(int, input().split()))

ans = 0

for i in range(N):
    if A_list[i] > 10:
        ans += (A_list[i]-10)

print(ans)
