#!/usr/bin/env python3

N = int(input())

S = list(input())
ans = ""
for i in range(N):
    if i == N-1:
        ans += S[i]
        break
    if S[i] + S[i+1] == 'na':
        ans += "ny"
    else:
        ans += S[i]

print(ans)
