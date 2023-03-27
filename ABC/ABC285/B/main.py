#!/usr/bin/env python3

N = int(input())
S = list(input())

for i in range(1, N):
    ans = 0
    for l in range(1, N-i+1):
        if S[l-1] != S[l+i-1]:
            ans = max(ans, l)
        else:

            break
    print(ans)

