#!/usr/bin/env python3
N = int(input())
A_list = list(map(int, input().split()))
ans = []
for x in A_list:
    if x % 2 == 0:
        ans.append(x)

print(*ans)
