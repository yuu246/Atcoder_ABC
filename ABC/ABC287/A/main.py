#!/usr/bin/env python3

N = int(input())

ans = 0
for _ in range(N):
    s = input()
    if s == 'For':
        ans += 1

if ans > (N // 2):
    print('Yes')
else:
    print('No')